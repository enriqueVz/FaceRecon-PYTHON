**---Español---**
Este proyecto ha sido desarrollado para realizar una detección y verificación facial a tiempo real.
Está escrito en Python, y he usado las librerías OpenCV (para capturar el vídeo) y DeepFace (para realizar la verificación facial).
He escogido el modelo "Facenet" debido a su menor costo computacional.

Funciona de la siguiente manera:

1) Se captura el vídeo a tiempo real gracias a OpenCV.
2) Se compara la cara detectada con la imagen de referencia.
3) Finalmente, se muestra en pantalla si hay una coincidencia o no.


Para probar el proyecto:

1) Instala las dependencias requeridas mediante este comando: **pip install opencv-python deepface**.
2) Añade un "selfie" (en formato .jpg) y almacena su ruta en la variable **"imagen_referencia"**.
3) Ejecuta el archivo desde la terminal: **Python3 "/Ruta/a/tu/carpeta/main.py"**.

**---English---**

This project has been developed for real-time face detection and verification.
It is written in Python and uses the OpenCV library (to capture video) and DeepFace (for facial verification).
I chose the "Facenet" model due to its lower computational cost.

How it works:

1) Captures real-time video using OpenCV.
2) Compares the detected face with a reference image.
3) Displays on screen whether there is a match or not.

How to test it:

1) Install the required dependencies with this command: **pip install opencv-python deepface**.
2) Add a selfie in **.jpg** format, and store its route on the variable **"imagen_referencia"**.
3) Run the script from the terminal: **Python3 "/Path/to/your/folder/main.py"**.
