# Author: Aishwarya Dekhane

#imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

def region_of_interest(image, vertices):
    #define mask
    mask = np.zeros_like(image)

    #create match color
    match_mask_color = 255

    #draw the polygon to mask the everything except region of interest
    cv2.fillPoly(mask, vertices, match_mask_color)

    #create masked image and return
    return cv2.bitwise_and(image, mask)

def draw_line(image, line_vectors):
    #take a copy of an image
    image_copy = np.copy(image)

    #create the blank image of the size of incoming image
    blank_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    #draw the lines
    for line in line_vectors:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=10)
    
    #merge the blank image with the original image and return
    return cv2.addWeighted(image, 0.8, blank_image, 1, 0.0)

def process(image):
    #find the shape of image
    height = image.shape[0]
    width = image.shape[1]

    #define the region of interest
    region_of_interest_vertices =[
        (0, height),
        (width/2, height/2),
        (width, height)
    ]

    #convert the image in the gray scale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #apply the canny edge detection
    canny_image = cv2.Canny(gray_image, 100, 100)

    #get the masked image
    masked_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    #apply the hough line transform
    hough_lines = cv2.HoughLinesP(masked_image, 
                                rho = 2, 
                                theta=np.pi / 60, 
                                threshold=50, 
                                lines=np.array([]), 
                                minLineLength = 40.0, 
                                maxLineGap = 100.0)

    #get the image with the lines drawn and return
    return draw_line(image, hough_lines)

#read the video
captured_video = cv2.VideoCapture('/Users/aishwaryadekhane/Desktop/Road_Lane_Line_Detection/Test_Sample/test_video.mp4')

while(captured_video.isOpened()):
    #read the video frame by frame
    ret, frame = captured_video.read()

    #get the frames with lines drawn
    frame = process(frame)

    #display the video frame by frame
    cv2.imshow('frame', frame)

    #add wait key for the termination of the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the captured video
captured_video.release()

#destroy all windows
cv2.destroyAllWindows()
