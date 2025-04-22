# 🍎 Clasificador de Frutas con Red Neuronal Convolucional 🍌

**Estudiante:** Aarón Enrique Ramírez González  

**Tarea:** Clasificación de objetos (clases) 

**Materia:** Sistemas de Visión Artificial  

## 📝 Descripción
Este repositorio contiene la implementación de una red neuronal convolucional (CNN) para la **clasificación de imágenes en tiempo real** capturadas desde la **webcam**, determinando si la fruta mostrada es una **manzana** o un **plátano**.

El proyecto incluye:

- 📸 **Captura de imágenes:** Captura personalizada de imágenes para cada clase usando la cámara integrada del equipo.
- 🧠 **Entrenamiento del modelo:** Implementación y entrenamiento de una CNN para clasificación binaria con TensorFlow/Keras.
- 📡 **Clasificación en vivo:** Uso de la webcam para predecir y mostrar la etiqueta de la fruta en pantalla.
- 🧾 **Estructura modular:** Código separado en archivos para mayor orden y facilidad de mantenimiento.

---

## 📋 Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes dependencias:

- **Python 3.12** (o una versión compatible)
- **OpenCV:** Para acceder a la webcam y manipular imágenes.
- **TensorFlow y Keras:** Para construir y entrenar el modelo de red neuronal.
- **NumPy:** Para manejo de arreglos y matrices.

Instalación rápida con:

```bash
pip install -r requirements.txt
```

```bash
Convolutive_neuronal_network
│
│
├── src/
│   ├── Capture_Manzana.py   # Captura imágenes de manzanas con la webcam
│   ├── Capture_Platano.py   # Captura imágenes de plátanos con la webcam
│   ├── Trained_model.py     # Entrena la red neuronal y guarda el modelo
│   └── Fruit_classifier.py  # Clasificador en tiempo real desde la webcam
│
├── Trained_model/
│   └── model.h5             # Modelo entrenado guardado automáticamente
│
├── .gitignore  #Para ignorar archivos no deseados
│
├── main.py                  # Script principal para ejecutar diferentes tareas
├── Requirements.txt         # Lista de dependencias necesarias
└── README.md                # Este documento
```
## 🚀 ¿Cómo usar este repositorio?
Sigue estos pasos para ejecutar el proyecto en tu equipo:

### Clona el repositorio 🖥️:
Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu computadora:

```bash
git clone https://github.com/Aaron040-Rmz/Conv_Neu_Netw_Apple_and_Banana
```
### Crea un nuevo entorno virtual:
Se recomienda crear un entorno virtual en la carpeta principal para un fácil acceso. 

### Instala las dependencias 📦:
Asegúrate de tener instaladas las bibliotecas necesarias. Ejecuta el siguiente comando para instalarlas:

```bash
pip install -r Requirements.txt
```
### Ejecuta el script principal 🚀:

1. Captura tus imágenes para entrenar.

Asegúrate de tener buena iluminación y que la fruta ocupe una porción clara del encuadre.

```bash
python main.py --step capture_manzana
python main.py --step capture_platano
```

Presiona s para tomar una imagen y q para salir cuando hayas capturado suficientes.

2. Entrena el modelo

```bash
python main.py --step train
```

Este comando entrenará la red neuronal y guardará el modelo en la carpeta `Trained_model`.

3. Ejecuta la clasificación en tiempo real

```bash
python main.py --step run
```

Muestra la predicción de la fruta en la cámara en tiempo real si el modelo está seguro (confianza ≥ 75%).

## 🧠 ¿Qué hace cada script?
* Capture_Manzana.py y Capture_Platano.py: Capturan imágenes con la webcam para entrenamiento.

* Trained_model.py: Construye y entrena una CNN usando imágenes del dataset.

* Fruit_classifier.py: Ejecuta el modelo entrenado para clasificar frutas en vivo.

* main.py: Orquestador general que permite ejecutar cualquier módulo con el parámetro --step.

## ✅ Resultados esperados
* Entrenamiento con imágenes reales personalizadas.

* Modelo capaz de distinguir entre una manzana y un plátano en tiempo real.

* Interfaz visual en la cámara que muestra la fruta reconocida si se detecta con alta confianza.

## 🛠️ Tecnologías Utilizadas
- **Python 3.12.4**

- **OpenCV**

- **TensorFlow y Keras**

- **NumPy**

- **Argparse** (para manejar desde main.py los distintos pasos)

## 🙏 Agradecimientos

Gracias por ver mi "Readme"! 😃

Que tengas un muy buen día y que Dios te bendiga en gran manera a ti y a toda tu familia.😊