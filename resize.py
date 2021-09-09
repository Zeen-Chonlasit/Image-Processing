import cv2
import matplotlib.pyplot as plt
import numpy as np

im = cv2.imread('Photo/cat.jpg') 
im= cv2.cvtColor(im, cv2.COLOR_BGR2RGB ) 
image = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

scale_percent = 60 # percent of original size 
width = int(image.shape[1] * scale_percent / 100) 
height = int(image.shape[0] * scale_percent / 100)

smaller = cv2.resize(image,(width, height)) 

plt.imshow(smaller, cmap='gray') 
plt.axis('off') 
plt.show()