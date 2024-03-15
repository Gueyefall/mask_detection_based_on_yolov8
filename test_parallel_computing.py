import torch
from ultralytics import YOLO

# Vérification de la disponibilité de CUDA (support GPU).
print("CUDA disponible :", torch.cuda.is_available())

# Réglage du périphérique sur GPU s'il est disponible.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Chargement du modèle YOLO.
model = YOLO("yolov8n.pt")

# Transfert du modèle sur le périphérique (GPU si disponible).
model.to(device)

# Vérification si le modèle utilise bien la GPU.
print(f"Le modèle est-il sur GPU ? {'Oui' if next(model.parameters()).is_cuda else 'Non'}")
