''' Training a model on mask detection '''
import torch
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8l.pt")

# Now, when performing inference or training, check if the model is on GPU
print(next(model.parameters()).is_cuda)

# Train the model
model.train(data="/home/pape/Documents/Esigelec/AD_DAS/Documents_TP_TD/Datasets/Mask_detection_dataset/data.yaml", device="cuda", epochs=30, workers=12, batch=16, imgsz=640, cache="disk")