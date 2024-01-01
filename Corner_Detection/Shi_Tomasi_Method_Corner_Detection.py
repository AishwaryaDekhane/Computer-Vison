#Author: Aishwarya Dekhane
#Date: 27th Dec, 2023

'''
What are corners? 
-   Corners are the region in the image with large variation in intensity in all the direction.
-   Now this Harris corner detector was first introduced by Chris Harris and Mike Steffens in their people in 1988.
'''

#imports
import cv2
import numpy as np

#read image
image = cv2.imread('/Users/aishwaryadekhane/Desktop/Corner_Detection/pic1.png')

#display image
cv2.imshow('original', image)

#convert the image to the gray scale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#apply the Sho-Tomasi Corner Detection method
detected_corners = cv2.goodFeaturesToTrack(image_gray, 25, 0.01, 10)

#conver the detected corners in the int
detected_corners = np.int64(detected_corners)

#iterate over the corners
for corner in detected_corners:
    #get the x and y
    x, y = corner.ravel()

    #draw circle
    cv2.circle(image, (x, y), 3, 255, -1)

#display image
cv2.imshow('output', image)

#add the wait key
cv2.waitKey(0)

#destroy all the windows
cv2.destroyAllWindows()
