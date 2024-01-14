#Author: Aishwarya Dekhane  
#Date: 14 Jan, 2024

import numpy as np
import cv2
from random import randint

img = cv2.imread("/Users/aishwaryadekhane/Desktop/Colorful_Clarity_FuzzyImage_Area_Segmentation_Recoloring/fuzzy.png",1)
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

thresh = cv2.adaptiveThreshold(
	blur, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("Thresh", thresh)

contours, hierarchy = cv2.findContours(
	thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

filtered = []
for c in contours:
	if cv2.contourArea(c) < 1000:
		continue
	filtered.append(c)
print(len(filtered))

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for c in filtered:
	col = (randint(0,255), randint(0,255), randint(0,255))
	cv2.drawContours(objects, [c], -1, col, -1)
	area = cv2.contourArea(c)
	print(area)

cv2.imshow("Final", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()