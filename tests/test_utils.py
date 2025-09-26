"""
Tests for utility functions
"""
import pytest
import torch
from PIL import Image
import numpy as np
from src.utils.device_utils import get_device, to_device
from src.utils.image_utils import preprocess_image, validate_image

class TestDeviceUtils:
    """Test cases for device utilities"""
    
    def test_get_device(self):
        """Test device detection"""
        device = get_device()
        assert device is not None
        assert isinstance(device, torch.device)
    
    def test_to_device_tensor(self):
        """Test moving tensor to device"""
        device = get_device()
        tensor = torch.randn(1, 3, 224, 224)
        moved_tensor = to_device(tensor, device)
        assert moved_tensor.device == device
    
    def test_to_device_list(self):
        """Test moving list of tensors to device"""
        device = get_device()
        tensors = [torch.randn(1, 3, 224, 224), torch.randn(1, 9)]
        moved_tensors = to_device(tensors, device)
        assert isinstance(moved_tensors, list)
        for tensor in moved_tensors:
            assert tensor.device == device

class TestImageUtils:
    """Test cases for image utilities"""
    
    def setup_method(self):
        """Set up test fixtures"""
        # Create a dummy PIL image
        self.test_image = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
    
    def test_preprocess_image(self):
        """Test image preprocessing"""
        processed = preprocess_image(self.test_image)
        assert processed.size == (224, 224)
        assert processed.mode == 'RGB'
    
    def test_validate_image_valid(self):
        """Test validation of valid image"""
        assert validate_image(self.test_image) == True
    
    def test_validate_image_too_small(self):
        """Test validation of too small image"""
        small_image = Image.fromarray(np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8))
        assert validate_image(small_image) == False
    
    def test_validate_image_too_large(self):
        """Test validation of too large image"""
        large_image = Image.fromarray(np.random.randint(0, 255, (6000, 6000, 3), dtype=np.uint8))
        assert validate_image(large_image) == False
    
    def test_preprocess_image_different_sizes(self):
        """Test preprocessing with different target sizes"""
        target_sizes = [(128, 128), (256, 256), (512, 512)]
        
        for size in target_sizes:
            processed = preprocess_image(self.test_image, target_size=size)
            assert processed.size == size
