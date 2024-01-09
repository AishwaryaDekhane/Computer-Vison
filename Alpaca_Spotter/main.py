#Author- Aishwarya Dekhane
#Date- 7 Jan,2024

from ultralytics import YOLO

#load model
model = YOLO("yolov8n.yaml")    #build a new model from scratch

#use model
results = model.train(data="config.yaml", epochs=1)    #train the model