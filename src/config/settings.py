"""
Configuration settings for the rice disease prediction application
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent.parent

# Model configuration
MODEL_CONFIG = {
    'model_path': os.path.join(BASE_DIR, 'model', 'resnet_Model.pth'),
    'input_size': (224, 224),
    'num_classes': 9,
    'in_channels': 3
}

# Class names for rice diseases
CLASS_NAMES = [
    'Neck_Blast',
    'Leaf scald',
    'Sheath Blight',
    'Healthy Rice Leaf',
    'Narrow Brown Leaf Spot',
    'Leaf Blast',
    'Rice Hispa',
    'Brown Spot',
    'Bacterial Leaf Blight'
]

# Image processing configuration
IMAGE_CONFIG = {
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'allowed_formats': ['jpg', 'jpeg', 'png', 'bmp', 'tiff'],
    'target_size': (224, 224),
    'normalize_mean': [0.5, 0.5, 0.5],
    'normalize_std': [0.5, 0.5, 0.5]
}

# Streamlit configuration
STREAMLIT_CONFIG = {
    'page_title': 'Rice Disease Prediction',
    'page_icon': '🌾',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S'
}

# File paths
PATHS = {
    'static_images': os.path.join(BASE_DIR, 'static', 'images'),
    'uploads': os.path.join(BASE_DIR, 'static', 'uploads'),
    'model_dir': os.path.join(BASE_DIR, 'model'),
    'docs': os.path.join(BASE_DIR, 'docs')
}

# Create directories if they don't exist
for path in PATHS.values():
    os.makedirs(path, exist_ok=True)
