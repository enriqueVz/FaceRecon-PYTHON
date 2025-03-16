import threading

import cv2

from deepface import DeepFace

captura = cv2.VideoCapture(0) #0 pilla la 1a camara

captura.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

contador = 0

cara_match = False

imagen_referencia = cv2.imread("/Users/kikon/IA PROJECTS/FACE RECOGNITION/reference.jpg")

def check_cara(frame):
    global cara_match
    try:
        if DeepFace.verify(frame, imagen_referencia.copy(), model_name="Facenet")['verified']:
            cara_match = True
        else:
            cara_match = False

    except ValueError:
        cara_match = False

while True:
    ret, frame = captura.read()

    if ret:
        if contador % 30 == 0:
            try:
                threading.Thread(target=check_cara, args=(frame.copy(),)).start()
            except ValueError: 
                pass

        contador += 1


        if cara_match:
            cv2.putText(frame, "Hola, Enrique!", (20,450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 255, 0), thickness = 3)
        else:
            cv2.putText(frame, "NO MATCH :(", (20,450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 255), thickness = 3)

        cv2.imshow("video", frame)



    tecla = cv2.waitKey(1)
    if tecla == ord("q"):
        break

cv2.destroyAllWindows()