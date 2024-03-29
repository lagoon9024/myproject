import cv2
import numpy as np
import os
import datetime
import MySQLdb
import time
import sys

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

db=MySQLdb.connect("70.12.111.177","tester","1234","db")
cur=db.cursor()


#iniciate id counter
id = 0

# names related to ids: example ==> loze: id=1,  etc
#names = ['None', 'LJH', 'kim', 'lee', 'ksw']
with open('name.txt','r') as f:
    names=f.readlines()
names=[line.rstrip('\n') for line in names]

print(names)

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW),int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        
        percent=confidence
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))

        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        #f=open('check.txt','a')
        #f.write(id+str(confidence)+'\n')
        #f.close()
        now=datetime.datetime.now()
        print(sys.argv[1])
        print("insert into detect values(%s,%s,%d,%s)"%(id,datetime.datetime.now(),percent,sys.argv[1]))
        try:
            cur.execute("insert into detectdata_detect(cname,ctime,cpercent,cid) values('%s','%s','%d','%s')"%(sys.argv[1],datetime.datetime.now(),100-percent,id))  
            print("success")
            db.commit()
            time.sleep(1)
        except:
            db.rollback()
        #time.sleep(1)
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()




