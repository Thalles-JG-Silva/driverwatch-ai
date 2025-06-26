# DriverWatch-AI

### 🧠 Sistema de detecção de sonolência e distração de motoristas com IA

---

## 🎯 Objetivo do Projeto

Monitorar o rosto do motorista em tempo real utilizando visão computacional e alertar em caso de sonolência ou se ele adormecer ao volante, ajudando a prevenir acidentes.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- Python 3
- OpenCV
- dlib
- NumPy
- scipy
- playsound

**Modelo de pontos faciais:** `shape_predictor_68_face_landmarks.dat`  
(Disponível em: [Download aqui](https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat))

---

## ⚙️ Descrição do Funcionamento

- O software utiliza a câmera do computador para capturar o rosto do motorista.
- Analisa os olhos com base na razão de aspecto (EAR).
- Se os olhos permanecerem fechados por alguns segundos, um **alerta leve** (alerta1.mp3) é tocado.
- Se os olhos permanecerem fechados por ainda mais tempo, um **alarme forte** (alerta2.mp3) é ativado.
- O sistema reinicia os contadores quando os olhos são abertos novamente.

---

## ▶️ Como Executar/Testar o Projeto

1. **Clone o repositório ou baixe os arquivos.**

2. **Instale as dependências:**

```bash
pip install opencv-python dlib numpy scipy playsound
