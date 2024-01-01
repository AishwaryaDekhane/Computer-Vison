#Author: Atharva Pore
#Date: 27th Dec, 2023

'''
Haar Cascade Detection:
-   So object detection using Haar feature based cascade classifiers is an effective object detection method 
    proposed by Paul Viola and Michael Jones in their people.
    Now Haar feature based cascade classifier is a machine learning based approach where a cascade function
    is trained for a lot of positive and negative images.
-   Now what are these positive and negative images.
    So first a classifier is trained with a few hundred simple views of particular object that is a face
    or a car or any other object that is called a positive example.
    So whatever you want to detect if you train your classifier with those kind of values.
    So for example if you want to detect face then you need to train your classifier with the number of
    images which contain faces.
    So these are called Positive images which contains the object which you want to detect.
    
    Similarly we want the classifier to train with the negative images. That means the images which doesn't 
    contain the object which you want to detect.
'''

#imports
import cv2

#define the classifier
haar_cascade_face = cv2.CascadeClassifier('/Users/atharvapore/Desktop/Masters/Projects/OpenCV/Project_2_FaceEyeDetection/haarcascade_frontalface_default.xml')
haar_cascade_eye = cv2.CascadeClassifier('/Users/atharvapore/Desktop/Masters/Projects/OpenCV/Project_2_FaceEyeDetection/haarcascade_eye_tree_eyeglasses.xml')

#read video
video = cv2.VideoCapture(0)

while video.isOpened():
    #get the frame
    ret, frame = video.read()

    #convert the frame to the gray scale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect the faces from the frame
    faces = haar_cascade_face.detectMultiScale(frame_gray, 1.1, minNeighbors=4)

    #iterate over the faces
    for (x, y, w, h) in faces:
        #draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #get the region of interest for eyes
        region_of_interest_gray = frame_gray[y:y+h, x:x+w]
        region_of_interest_color = frame[y:y+h, x:x+w]

        #detect the eyes from the frame
        eyes = haar_cascade_eye.detectMultiScale(region_of_interest_gray)

        #iterate over the faces
        for (ex, ey, ew, eh) in eyes:
            #draw rectangle
            cv2.rectangle(region_of_interest_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

    #display frame
    cv2.imshow('output', frame)

    #add the wait key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the video context
video.release()

#destroy all the windows
cv2.destroyAllWindows()
