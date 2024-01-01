#Author: Aishwarya Dekhane
#Date: 27th Dec, 2023

'''
What are corners? 
-   Corners are the region in the image with large variation in intensity in all the direction.
-   Now this Harris corner detector was first introduced by Chris Harris and Mike Steffens in their people in 1988.

Steps for the Harris Corner Detection:
1. Determine which windows produces very large variation in intensity when we move in the "x" direction and the "y" direction.
2. With each such window found, score R is computed.
3. After applying the threshold to this score, important corners are selected and marked.
'''

#imports
import cv2
import numpy as np

#read image
image = cv2.imread('/Users/aishwaryadekhane/Desktop/Corner_ Detection/chessboard.png')

#display image
cv2.imshow('original', image)

#convert the image to the gray scale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#convert the gray scale image array to float 32 because the Harris corner detection method takes the image in this format
image_gray = np.float32(image_gray)

#apply the corner harris method on image
output_image = cv2.cornerHarris(image_gray, 2, 3, 0.04)

#apply the dilation on the output image
output_image = cv2.dilate(output_image, None)

#reverting back to the original image with optimal threshol value
image[output_image > 0.01 * output_image.max()] = [0, 0, 255]

#display image
cv2.imshow('output', image)

#add the wait key
cv2.waitKey(0)

#destroy all the windows
cv2.destroyAllWindows()
