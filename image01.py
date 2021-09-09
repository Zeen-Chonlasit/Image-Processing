import cv2

import matplotlib.pyplot as plt



img1 = cv2.imread("template.png ")

img2 = cv2.imread("qrcode01.png")



img1[0:42,0:36] = img2



cv2.imshow("my template",img1)



cv2.waitKey(0)

cv2.destroyAllWindows()