#Author: Aishwarya Dekhane  
#Date: 13 Jan, 2024

import numpy as np
import cv2

#catpturing video
cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()     #always read new frame and load that as image

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)     #fx,fy
	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)     #run key -run every 1 sec
	if ch & 0xFF == ord('q'):   #q ro break the loop
		break

cap.release()
cv2.destroyAllWindows()