"""
Image processing utilities
"""
import cv2
import numpy as np
from PIL import Image
import streamlit as st
from typing import Optional, Tuple

def preprocess_image(image: Image.Image, target_size: Tuple[int, int] = (224, 224)) -> Image.Image:
    """
    Preprocess image for model input
    
    Args:
        image: PIL Image object
        target_size: Target size for resizing (width, height)
    
    Returns:
        Preprocessed PIL Image
    """
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize image
    image = image.resize(target_size, Image.Resampling.LANCZOS)
    
    return image

def validate_image(image: Image.Image) -> bool:
    """
    Validate if image is suitable for processing
    
    Args:
        image: PIL Image object
    
    Returns:
        True if image is valid, False otherwise
    """
    # Check if image has valid dimensions
    if image.size[0] < 50 or image.size[1] < 50:
        return False
    
    # Check if image is not too large (to prevent memory issues)
    if image.size[0] > 5000 or image.size[1] > 5000:
        return False
    
    return True

def display_image_info(image: Image.Image) -> None:
    """
    Display image information in Streamlit
    
    Args:
        image: PIL Image object
    """
    st.write(f"**Image Size:** {image.size[0]} x {image.size[1]} pixels")
    st.write(f"**Image Mode:** {image.mode}")
    st.write(f"**Image Format:** {image.format if hasattr(image, 'format') else 'Unknown'}")

def enhance_image(image: Image.Image) -> Image.Image:
    """
    Apply basic image enhancement
    
    Args:
        image: PIL Image object
    
    Returns:
        Enhanced PIL Image
    """
    # Convert to numpy array for OpenCV processing
    img_array = np.array(image)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    lab = cv2.cvtColor(img_array, cv2.COLOR_RGB2LAB)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    
    return Image.fromarray(enhanced)
