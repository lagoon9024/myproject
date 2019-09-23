import numpy as numpy
import cv2

img = cv2.imread('Lenna.png',0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.startWindowThread()
cv2.namedWindow("preview")
cv2.imshow("preview",img)