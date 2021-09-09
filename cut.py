import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Photo/cat.jpg')
type(img)
#cv2.imwrite("Photo/new_cat.jpg",img)
ans1 = img[200:2300,1200:3200]

ans2 = img[1500:3000,3100:5200]

img.shape

cv2.imwrite("Photo/new_cat1.jpg",ans1)
plt.imshow(ans1)
plt.show()
cv2.imwrite("Photo/new_cat2.jpg",ans2)
plt.imshow(ans2)
plt.show()