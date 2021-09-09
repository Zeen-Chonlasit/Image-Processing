import cv2
import qrcode

#Creating an instance of qrcode
input_data = "รหัสนิสิต 6121614218 ชื่อ นราธิป ร่มโพธิ์"
qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color='white')
img.save('6121614218.png')