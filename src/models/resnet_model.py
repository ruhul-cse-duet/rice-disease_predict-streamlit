"""
Custom ResNet model for rice disease prediction
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageClassificationBase(nn.Module):
    """Base class for image classification models"""
    
    def training_step(self, batch):
        images, labels = batch
        out = self(images)
        loss = F.cross_entropy(out, labels)
        return loss

    def validation_step(self, batch):
        images, labels = batch
        out = self(images)
        loss = F.cross_entropy(out, labels)
        acc = self.accuracy(out, labels)
        return {'val_loss': loss.detach(), 'val_acc': acc}

    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()
        batch_accs = [x['val_acc'] for x in outputs]
        epoch_acc = torch.stack(batch_accs).mean()
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}

    def epoch_end(self, epoch, result):
        logger.info("Epoch [{}], train_loss: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}".format(
            epoch, result['train_loss'], result['val_loss'], result['val_acc']))

    def accuracy(self, outputs, labels):
        _, preds = torch.max(outputs, dim=1)
        return torch.tensor(torch.sum(preds == labels).item() / len(preds))


def ConvBlock(in_channels, out_channels, pool=False):
    """Convolution block with BatchNormalization"""
    layers = [nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
              nn.BatchNorm2d(out_channels),
              nn.ReLU(inplace=True)]
    if pool:
        layers.append(nn.MaxPool2d(4))
    return nn.Sequential(*layers)


class CNN_NeuralNet(ImageClassificationBase):
    """Custom CNN with ResNet architecture for rice disease classification"""
    
    def __init__(self, in_channels, num_diseases):
        super().__init__()
        
        self.conv1 = ConvBlock(in_channels, 64)
        self.conv2 = ConvBlock(64, 128, pool=True)
        self.res1 = nn.Sequential(ConvBlock(128, 128), ConvBlock(128, 128))
        
        self.conv3 = ConvBlock(128, 256, pool=True)
        self.conv4 = ConvBlock(256, 512, pool=True)
        
        self.res2 = nn.Sequential(ConvBlock(512, 512), ConvBlock(512, 512))
        
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(512, num_diseases)
        )

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.res1(out) + out
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.res2(out) + out
        out = self.classifier(out)
        return out


class RiceDiseasePredictor:
    """Main class for rice disease prediction"""
    
    def __init__(self, model_path='model/resnet_Model.pth', device=None):
        self.device = device or torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self._load_model(model_path)
        self.transform = self._get_transform()
        
    def _load_model(self, model_path):
        """Load the trained model"""
        try:
            model = CNN_NeuralNet(3, 9)
            model = model.to(self.device)
            model.load_state_dict(torch.load(model_path, weights_only=True, map_location=self.device))
            model.eval()
            logger.info(f"Model loaded successfully from {model_path}")
            return model
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def _get_transform(self):
        """Get image transformation pipeline"""
        return transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])
    
    def predict(self, image):
        """Predict disease from image"""
        try:
            # Transform image
            image_tensor = self.transform(image)
            image_tensor = image_tensor.unsqueeze(0).to(self.device)
            
            # Make prediction
            with torch.no_grad():
                output = self.model(image_tensor)
                predicted = output.argmax(dim=1).item()
            
            return predicted
        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            raise
