#Author: Aishwarya Dekhane
#Date: 26th Dec, 2023

'''
Note: To run this code I have used 'pip install opencv-contrib-python'
'''

#imports
import cv2
import numpy as np

#capture video
video = cv2.VideoCapture('/Users/aishwaryadekhane/Desktop/Background_Removal/vtest.avi')

#define kernel only for createBackgroundSubtractorGMG
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

#get the foreground and the background
#foreground_background = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#foreground_background = cv2.bgsegm.createBackgroundSubtractorGMG()
foreground_background = cv2.createBackgroundSubtractorKNN()
#foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG() #gaussian method is used inside this to get the foreground and the background

while video.isOpened():
    #read the frame
    ret, frame = video.read()

    #create the foreground mask
    fg_mask = foreground_background.apply(frame)

    #apply thr morphology only for createBackgroundSubtractorGMG
    #fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

    #display the video
    cv2.imshow('original', frame)
    cv2.imshow('fg_mask', fg_mask)

    #add wait key for the termination of the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the captured video
video.release()

#destroy all windows
cv2.destroyAllWindows()
