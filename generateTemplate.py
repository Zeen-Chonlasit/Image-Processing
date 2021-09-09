import cv2
import numpy

img = cv2.imread('D:\DIP_semesterii2563\mypic.jpg')
tile = numpy.tile(img,(6,4,1))


cv2.imshow("Mypic",tile)
cv2.imwrite("MyPic.png",tile)
cv2.waitKey(0)
cv2.destroyAllWindows()
