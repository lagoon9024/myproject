import cv2
import sys

#imagePath = './Lenna.png'
#cascPath = sys.argv[1]
cascPath = './haarcascades/haarcascade_frontalface_default.xml' 

faceCascade = cv2.CascadeClassifier(cascPath)

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret,img=cap.read()
    img=cv2.flip(img,-1) #up/down
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
   # flags = cv2.CASCADE_SCALE_IMAGE
    )

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
    cv2.imshow("Faces Found", img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
