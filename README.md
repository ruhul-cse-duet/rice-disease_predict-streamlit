# Rice Disease Prediction System 🌾

A deep learning-based web application for identifying rice diseases using computer vision and providing treatment recommendations. The system uses a custom ResNet architecture to classify rice leaf images into 9 different disease categories.

## Features

- 🔍 **Disease Detection**: Identify 9 different rice diseases with high accuracy
- 🌱 **Treatment Recommendations**: Get detailed treatment suggestions in Bengali
- 📱 **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- 🚀 **Fast Predictions**: Real-time disease classification
- 🐳 **Docker Support**: Easy deployment with Docker and Docker Compose
- ☁️ **Cloud Ready**: Deployable on various cloud platforms

## Supported Diseases

1. **Neck Blast** (গোড়ার দাগ রোগ)
2. **Leaf Scald** (পাতা পুড়ে যাওয়া রোগ)
3. **Sheath Blight** (পাতার গোড়া পচা রোগ)
4. **Healthy Rice Leaf** (সুস্থ ধানের পাতা)
5. **Narrow Brown Leaf Spot** (পাতায় সরু বাদামী দাগ)
6. **Leaf Blast** (পাতায় দাগ রোগ)
7. **Rice Hispa** (রাইস হিছপা কীট আক্রমণ)
8. **Brown Spot** (পাতায় বাদামী দাগ রোগ)
9. **Bacterial Leaf Blight** (পাতা পঁচা ব্যাকটেরিয়া রোগ)

## Project Structure

```
Rice Disease Prediction/
├── src/
│   ├── models/
│   │   └── resnet_model.py          # Custom ResNet model
│   ├── services/
│   │   └── treatment_service.py     # Treatment recommendations
│   ├── utils/
│   │   ├── device_utils.py          # Device management
│   │   └── image_utils.py           # Image processing
│   ├── config/
│   │   └── settings.py              # Configuration settings
│   └── app.py                       # Main Streamlit application
├── model/
│   └── resnet_Model.pth             # Trained model weights
├── static/
│   ├── images/                      # Static images
│   └── uploads/                     # User uploads
├── tests/                           # Unit tests
├── docs/                           # Documentation
├── requirements.txt                 # Python dependencies
├── Dockerfile                      # Docker configuration
├── docker-compose.yml              # Docker Compose setup
├── nginx.conf                      # Nginx configuration
└── README.md                       # This file
```

## Installation

### Prerequisites

- Python 3.9+
- Docker (optional)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rice-disease-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run src/app.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:8501`

### Docker Deployment

1. **Build and run with Docker**
   ```bash
   docker build -t rice-disease-app .
   docker run -p 8501:8501 rice-disease-app
   ```

2. **Using Docker Compose**
   ```bash
   # Development
   docker-compose up --build
   
   # Production with Nginx
   docker-compose --profile production up --build
   ```

## Usage

1. **Upload Image**: Go to the "Disease Recognition" page and upload a rice leaf image
2. **Get Prediction**: Click the "Predict" button to analyze the image
3. **View Results**: See the predicted disease and treatment recommendations
4. **Treatment Guide**: Follow the detailed treatment suggestions provided

## Model Architecture

The system uses a custom ResNet (Residual Network) architecture specifically designed for rice disease classification:

- **Input**: 224×224 RGB images
- **Architecture**: Custom CNN with ResNet blocks
- **Classes**: 9 disease categories
- **Features**: Skip connections, batch normalization, adaptive pooling

## API Endpoints

The application provides a web interface with the following pages:

- **Home**: Introduction and overview
- **About**: Dataset information and model details
- **Disease Recognition**: Image upload and prediction interface

## Configuration

Key configuration options can be modified in `src/config/settings.py`:

- Model path and parameters
- Image processing settings
- Streamlit configuration
- Logging settings

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src/
```

### Code Style

The project follows PEP 8 style guidelines. Use the following tools:

```bash
# Format code
black src/

# Lint code
flake8 src/

# Type checking
mypy src/
```

## Deployment

### Cloud Platforms

#### Heroku
1. Create a `Procfile`:
   ```
   web: streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Deploy:
   ```bash
   git push heroku main
   ```

#### AWS/GCP/Azure
1. Use Docker containers
2. Configure load balancer
3. Set up SSL certificates
4. Configure environment variables

### Environment Variables

- `STREAMLIT_SERVER_PORT`: Port number (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: 0.0.0.0)
- `MODEL_PATH`: Path to the trained model file

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset: Rice disease images from various agricultural sources
- Model: Custom ResNet architecture inspired by Microsoft's ResNet
- Framework: Streamlit for web interface, PyTorch for deep learning

## Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation in the `docs/` folder

## Changelog

### Version 1.0.0
- Initial release
- Custom ResNet model implementation
- Streamlit web interface
- Docker support
- Treatment recommendations in Bengali
