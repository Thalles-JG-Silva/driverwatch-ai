# 🚗👁️🧠 DriverWatch-AI

## 🎯 Objetivo do Projeto

Monitorar, em tempo real, sinais de sonolência do motorista utilizando visão computacional. O sistema emite alertas sonoros progressivos ao detectar olhos fechados por períodos prolongados, ajudando a prevenir acidentes.

---

## 🛠 Tecnologias e Ferramentas Utilizadas

- Python 3.10
- OpenCV (cv2)
- dlib
- NumPy
- SciPy
- Pygame

---

## ⚙️ Descrição do Funcionamento

1. O sistema usa a webcam para capturar o rosto do motorista em tempo real.
2. A biblioteca `dlib` identifica os olhos com base no modelo `shape_predictor_68_face_landmarks.dat`.
3. A razão de aspecto dos olhos (EAR) é calculada para verificar se estão fechados.
4. Dois níveis de alerta sonoro são acionados:
   - **Alerta leve**: olhos fechados por um curto período.
   - **Alarme forte**: olhos fechados por um tempo prolongado.
5. Os sons são tocados usando `pygame` sem travar a interface.

---

## ▶️ Como Executar/Testar o Projeto

### Pré-requisitos

- Python 3.10 instalado
- Webcam funcional
- As bibliotecas abaixo instaladas:

```bash
pip install opencv-python dlib scipy numpy pygame
```

### Passo a Passo

1. Clone o repositório ou baixe os arquivos.
2. Certifique-se de que os seguintes arquivos estejam na pasta raiz do projeto:
   - `driverwatch_ai.py`
   - `alerta1.wav` (alerta sonoro leve)
   - `alerta2.wav` (alarme sonoro forte)
   - `shape_predictor_68_face_landmarks.dat` (modelo de pontos faciais)

3. Execute o script:

```bash
python driverwatch_ai.py
```

4. Uma janela será aberta com a imagem da webcam.
   - Pressione `q` para sair.

---

### Passo a Passo

## 📝 Observações

- O sistema é apenas uma demonstração e não substitui ferramentas profissionais de segurança veicular.
