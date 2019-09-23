import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Lenna.png')
b,g,r = cv2.split(img)
img2 = img[:,:,::-1]

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img2)
plt.show()

key=cv2.waitKey(0)

if key==27:
    cv2.destroyAllWindows()