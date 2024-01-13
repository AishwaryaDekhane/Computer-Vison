#Author: Aishwarya Dekhane  
#Date: 12 Jan, 2024

import numpy as np
import cv2

image = cv2.imread("/Users/aishwaryadekhane/Desktop/thresh.jpg")
cv2.imshow("Original",image)

#how much to blur value- odd values - 5,55-x,y
blur = cv2.GaussianBlur(image, (5,55),0)
cv2.imshow("Blur",blur)

kernel = np.ones((5,5),'uint8')

dilate = cv2.dilate(image,kernel,iterations=1)
erode = cv2.erode(image,kernel,iterations=1)

cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()