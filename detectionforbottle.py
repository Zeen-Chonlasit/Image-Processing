import numpy as np
import cv2
import matplotlib.pyplot as plt
#img = cv2.imread('images/coins.tif')
img = cv2.imread('Photo/bottle1.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #1 ได้ภาพโทนเทา
# print(img.shape) #(384, 384)
# โทนสีหนักหรือโทรสีเบา

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
plt.imshow(thresh, cmap='gray')

kernal = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernal,iterations=2)
plt.imshow(thresh, cmap='gray')

sure_bg = cv2.dilate(opening,kernal,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers ==-1] = [0,255,0]

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()