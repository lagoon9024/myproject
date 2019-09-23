import cv2
import numpy as np
img = cv2.imread('Lenna.png')

rows, cols = img.shape[:2]

M=np.float32([[1,0,40],[0,1,40]])

dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Original',img)
cv2.imshow('Traslation',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()