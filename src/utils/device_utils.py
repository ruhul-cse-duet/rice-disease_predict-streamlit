"""
Device utilities for model operations
"""
import torch
import logging

logger = logging.getLogger(__name__)

def get_device():
    """Get the best available device (CUDA or CPU)"""
    if torch.cuda.is_available():
        device = torch.device("cuda")
        logger.info(f"Using CUDA device: {torch.cuda.get_device_name()}")
    else:
        device = torch.device("cpu")
        logger.info("Using CPU device")
    
    return device

def to_device(data, device):
    """Move tensor(s) to chosen device"""
    if isinstance(data, (list, tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)
