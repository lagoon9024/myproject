import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)
cascPath = '/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(cascPath)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    for(x,y,w,h) in faces:
      cv2.rectangle(gray,(x,y),(x+w,y+h), (0,255,0),2)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()