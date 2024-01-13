#Author: Aishwarya Dekhane  
#Date: 12 Jan, 2024

import numpy as np
import cv2

color = cv2.imread('/Users/aishwaryadekhane/Desktop/butterfly.jpg',1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite('/Users/aishwaryadekhane/Desktop/gray.jpg',gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

#r,g,b,transparency
rgba = cv2.merge((b,g,r,g))
cv2.imwrite('/Users/aishwaryadekhane/Desktop/rgba.png',rgba)
