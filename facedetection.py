import cv2
import numpy as np
import time

faces  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCam = cv2.VideoCapture(1)

if not videoCam.isOpened():
    print("No camera found")
    exit()

q = False
while (q == False):
    ret, cap1 = videoCam.read()
    cap = cv2.flip(cap1, 1)

    if ret == True:
        textcolor = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        face = faces.detectMultiScale(textcolor, scaleFactor = 3, minNeighbors = 2)

        for (x, y, w, h) in face:
            cv2.rectangle(cap, (x, y), (x + w, y + h), (255, 255, 0), 2)
        
        count = "faces = " + str(len(face))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(cap, count, (0, 30), font, 1, (255, 0, 255), 3)

        cv2.imshow("Image", cap)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tombolQditekan = True
            break


videoCam.release()
cv2.destroyAllWindows()