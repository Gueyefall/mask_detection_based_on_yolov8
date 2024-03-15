''' Training a model on mask detection '''
import torch
from ultralytics import YOLO, settings

torch.cuda.empty_cache()

# Load the YOLO model
model = YOLO("yolov8m.pt", task="detect")

# Update configuration for data destination and Tensorboard use.
settings.update({
    #'runs_dir': '/path/to/runs', # Uncomment and adjust if necessary.
    'tensorboard': True  # Activate Tensorboard for visualization.
})

# Now, when performing inference or training, check if the model is on GPU
print(next(model.parameters()).is_cuda)

# Train the model
model.train(data="/home/pape/Documents/Esigelec/AD_DAS/Documents_TP_TD/Datasets/Mask_detection_dataset/data.yaml", 
            device="cuda", 
            epochs=30, 
            workers=12, 
            batch=16, 
            imgsz=640, 
            cache="disk")

# Training successfully completed.