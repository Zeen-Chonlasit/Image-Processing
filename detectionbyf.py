import cv2
image = cv2.imread('Photo/2.jpg')

# #กำหนดตัวแปรเปลี่ยนขนาดภาพ
# scale_percent = 20 # percent of original size
# width = int(image.shape[1] * scale_percent / 100)
# height = int(image.shape[0] * scale_percent / 100)
# dim = (width, height)

# #คำสั่งเปลี่ยนขนาดภาพ
# image2 = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
face  = face_cascade.detectMultiScale(image, scaleFactor = 1.8, minNeighbors = 20)
smiles  = smile_cascade.detectMultiScale(image, scaleFactor = 1.8, minNeighbors = 20)




 
for (sx, sy, sw, sh) in face:
           cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (0, 255,0), 5) 

for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (0, 255,0), 5)
 
 
 
cv2.imshow("Smile Detected", image)

 
 
cv2.waitKey(0)
cv2.destroyAllWindows()