import cv2
import dlib
import time
import numpy as np
from scipy.spatial import distance
import pygame
import threading

# Inicializa o mixer de som do pygame
pygame.mixer.init()

# Função para tocar o som em paralelo
def play_sound(path):
    def _play():
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    threading.Thread(target=_play, daemon=True).start()

# Função para calcular a razão de aspecto dos olhos
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Inicializa o detector de rosto e o preditor de pontos faciais
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Índices dos pontos dos olhos direito e esquerdo
left_eye_idx = list(range(42, 48))
right_eye_idx = list(range(36, 42))

# Inicializa a webcam
cap = cv2.VideoCapture(0)

# Parâmetros de detecção
EAR_THRESHOLD = 0.25         # Limite para considerar olho fechado
EAR_CONSEC_FRAMES = 20       # Frames para alerta
SLEEP_FRAMES = 48            # Frames para alarme

frame_counter = 0
alert_state = "normal"       # Estados: normal, alerta, alarme

print("DriverWatch-AI iniciado. Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in left_eye_idx])
        right_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in right_eye_idx])

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        ear = (left_ear + right_ear) / 2.0

        if ear < EAR_THRESHOLD:
            frame_counter += 1

            if EAR_CONSEC_FRAMES < frame_counter < SLEEP_FRAMES:
                cv2.putText(frame, "ALERTA: SONOLENCIA DETECTADA!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                if alert_state != "alerta":
                    play_sound("alerta1.wav")
                    alert_state = "alerta"

            elif frame_counter >= SLEEP_FRAMES:
                cv2.putText(frame, "ALARME: MOTORISTA DORMINDO!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                if alert_state != "alarme":
                    play_sound("alerta2.wav")
                    alert_state = "alarme"
        else:
            frame_counter = 0
            alert_state = "normal"

        # Desenha os contornos dos olhos
        cv2.polylines(frame, [left_eye], True, (0, 255, 0), 1)
        cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1)

    cv2.imshow("DriverWatch-AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera recursos
cap.release()
cv2.destroyAllWindows()
