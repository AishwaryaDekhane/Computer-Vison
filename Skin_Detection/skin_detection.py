#Author: Aishwarya Dekhane  
#Date: 13 Jan, 2024

import numpy as np
import cv2

img = cv2.imread('/Users/aishwaryadekhane/Desktop/faces.jpeg',1)

#convert to HSV file format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#split channels
h = hsv[:,:,0]  #hue
s = hsv[:,:,1]  #saturation
v = hsv[:,:,2]  #value

#display channels
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV",hsv_split)

#provide saturation channel value>40 will appear white
ret, min_sat = cv2.threshold(s,40,255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter",min_sat)

#value channel- inverse of normal thresholding
ret, max_hue = cv2.threshold(h,15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter",max_hue)

final = cv2.bitwise_and(min_sat,max_hue)
cv2.imshow("Final",final)
cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
