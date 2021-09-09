import cv2
import numpy as np
template = cv2.imread("template.png",0) 
qrcode = cv2.imread("6121600217.png",0)
w, h = qrcode.shape
template[10:w+10,10:h+10] = qrcode

owner = "Khun.chonlasit Ratpongthon"
receiver = "Khun.Nikom Putajarn"

transfer = str(10500) 
cv2.putText(template,owner,(0,600),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
cv2.putText(template,receiver,(0,700),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
cv2.putText(template,transfer,(0,800),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))

image = cv2.line(template,  (0, 550) ,(600, 550) ,(0, 255, 0) , 2)
image = cv2.line(template,  (0, 750) ,(650, 750) ,(0, 255, 0) , 2)

cv2.imwrite("slip.png",template)
cv2.imshow("my slip",template)
cv2.waitKey(0)
cv2.destroyAllWindows()
