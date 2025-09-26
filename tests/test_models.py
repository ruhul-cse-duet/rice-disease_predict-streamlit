"""
Tests for model components
"""
import pytest  # pyright: ignore[reportMissingImports]
import torch
from src.models.resnet_model import CNN_NeuralNet, RiceDiseasePredictor
from src.config.settings import CLASS_NAMES

class TestCNN_NeuralNet:
    """Test cases for CNN_NeuralNet model"""
    
    def test_model_initialization(self):
        """Test model initialization"""
        model = CNN_NeuralNet(in_channels=3, num_diseases=9)
        assert model is not None
        assert isinstance(model, CNN_NeuralNet)
    
    def test_model_forward_pass(self):
        """Test model forward pass"""
        model = CNN_NeuralNet(in_channels=3, num_diseases=9)
        model.eval()
        
        # Create dummy input
        dummy_input = torch.randn(1, 3, 224, 224)
        
        with torch.no_grad():
            output = model(dummy_input)
        
        assert output.shape == (1, 9)  # batch_size, num_classes
    
    def test_model_parameters(self):
        """Test model has trainable parameters"""
        model = CNN_NeuralNet(in_channels=3, num_diseases=9)
        params = list(model.parameters())
        assert len(params) > 0
        
        # Check that parameters require gradients
        for param in params:
            assert param.requires_grad

class TestRiceDiseasePredictor:
    """Test cases for RiceDiseasePredictor"""
    
    def test_predictor_initialization(self):
        """Test predictor initialization without model file"""
        # This test will fail if model file doesn't exist
        # In a real scenario, you'd mock the model loading
        with pytest.raises(Exception):
            predictor = RiceDiseasePredictor(model_path='nonexistent_model.pth')
    
    def test_class_names(self):
        """Test that class names are properly defined"""
        assert len(CLASS_NAMES) == 9
        assert 'Healthy Rice Leaf' in CLASS_NAMES
        assert 'Neck_Blast' in CLASS_NAMES
        assert 'Leaf Blast' in CLASS_NAMES
