Este proyecto ha sido desarrollado para realizar una detección y verificación facial a tiempo real.
Está escrito en Python, y he usado las librerías OpenCV (para capturar el vídeo) y DeepFace (para realizar la verificación facial).
He escogido el modelo "Facenet" debido a su menor costo computacional.

Funciona de la siguiente manera:

1) Se captura el vídeo a tiempo real gracias a OpenCV.
2) Se compara la cara detectada con la imagen de referencia.
3) Finalmente, se muestra en pantalla si hay una coincidencia o no.


Para probar el proyecto:

1) Instala las dependencias requeridas mediante: **pip install opencv-python deepface**.
2) Añade un "selfie" (en formato .jpg) y almacena su ruta en la variable **"imagen_referencia"**.
3) Ejecuta el archivo desde la terminal: **Python3 "/Ruta/a/tu/carpeta/main.py"**.
