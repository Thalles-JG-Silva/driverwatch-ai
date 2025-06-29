# 🚗 DriverWatch-AI

## 🎯 Objetivo do Projeto

Detectar sinais de sonolência em motoristas em tempo real por meio de visão computacional, emitindo alertas sonoros que ajudam a prevenir acidentes causados por fadiga ao volante.

---

## 🛠 Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.10

* **Bibliotecas:**

  * OpenCV – captura e processamento de vídeo
  * Dlib – detecção facial e pontos faciais
  * NumPy e SciPy – cálculos matemáticos
  * Pygame – reprodução de áudio

* **Modelo pré-treinado incluso:**

  * `shape_predictor_68_face_landmarks.dat`

---

## ⚙️ Descrição do Funcionamento

1. O sistema utiliza a webcam para monitorar continuamente o rosto do motorista.
2. Detecta os olhos com base nos pontos faciais definidos pelo modelo.
3. Calcula a **razão de aspecto ocular (EAR)** para identificar se os olhos estão fechados.
4. A lógica de alerta segue os seguintes critérios:

   * **Olhos fechados por curto tempo:** emite **alerta leve** (`alerta1.wav`).
   * **Olhos fechados por tempo prolongado:** emite **alarme forte** (`alerta2.wav`).
5. Quando os olhos são reabertos, o contador é resetado.

---

## ▶️ Como Executar/Testar o Projeto

### ✅ Pré-requisitos

* Python 3.10 instalado
* Sistema operacional: **Windows** (ambiente testado)
* Ambiente virtual (venv) configurado com as dependências
* O arquivo `shape_predictor_68_face_landmarks.dat` já está incluído na pasta do projeto

### 📦 Passos para execução

1. **Abra o terminal e ative o ambiente virtual:**

```bash
cd caminho/para/o/projeto
.\driverwatch-env\Scripts\activate
```

2. **Instale as bibliotecas necessárias:**

```bash
pip install dlib-bin
pip install scipy opencv-python numpy pygame
```

3. **Execute o script principal:**

```bash
python driverwatch_ai.py
```
---
## ✅ Resultados obtidos

4. A janela com o vídeo será exibida. Pressione **'q'** para sair.
