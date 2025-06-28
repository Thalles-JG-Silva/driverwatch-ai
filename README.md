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
## Pré-requisitos

* Python 3.10 instalado no sistema
* Ambiente virtual (`venv`) criado no projeto (pasta `driverwatch-env`)
* Windows (testado)

---

1. **Clone o repositório ou baixe os arquivos.**

2. **Instale as dependências:**
---
Navegue até a pasta do projeto que contém o script principa

```
cd C: Pasta do projeto que contém o script principal
```
Ative o ambiente virtual
```
..\driverwatch-env\Scripts\activate
```
-  **O prompt deve exibir `(driverwatch-env)` indicando que o ambiente está ativo.**
  
Instale o pacote pré-compilado do dlib para evitar erros de compilação:
```
pip install dlib-bin
```
Instale as demais bibliotecas necessárias:
```
pip install scipy opencv-python numpy playsound
```
Execute o script
```
python driverwatch_ai.py
```
---
## 🎯 Resultados obtidos


