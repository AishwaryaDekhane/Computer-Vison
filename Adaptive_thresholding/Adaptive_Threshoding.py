#Author: Aishwarya Dekhane  
#Date: 13 Jan, 2024

import numpy as np
import cv2

img = cv2.imread('/Users/aishwaryadekhane/Desktop/sudoku.png',0)
cv2.imshow("Original",img)

#70=thresholding value, 255=unsigned int- max thresh
ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary",thresh_basic)

thres_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Threshold",thres_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()