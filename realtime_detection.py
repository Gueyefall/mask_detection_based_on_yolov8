''' For input video '''
import torch
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("mask_train_with_yolov8m/weights/best.pt")

# Now, when performing inference or training, check if the model is on GPU
print(next(model.parameters()).is_cuda)

''' The recommended approach is to use stream=True when calling model.predict() to avoid this issue.'''
# Predict using a video file with streaming to avoid RAM accumulation
results = model.predict(source="1", 
                        device="cuda", 
                        save=False, 
                        show=True, 
                        stream=True, 
                        show_conf=False)

# Now, when performing inference or training, check if the model is on GPU
print(next(model.parameters()).is_cuda)

''' By iterating over the results as they are generated (stream=True), you avoid loading all the data into memory at once.'''
# Process the results frame by frame
for r in results:
    boxes = r.boxes  # Boxes object for bbox outputs
