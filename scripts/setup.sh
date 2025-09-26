#!/bin/bash

# Rice Disease Prediction Setup Script
# This script sets up the development environment

set -e

echo "🌾 Setting up Rice Disease Prediction System..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.9"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION+ is required. Current version: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p static/images static/uploads tests docs

# Copy images if they exist
if [ -d "image" ]; then
    echo "🖼️ Copying images..."
    cp -r image/* static/images/ 2>/dev/null || true
fi

if [ -d "uploads" ]; then
    echo "📤 Copying uploads..."
    cp -r uploads/* static/uploads/ 2>/dev/null || true
fi

# Create .gitkeep files
touch static/uploads/.gitkeep

# Check if model file exists
if [ ! -f "model/resnet_Model.pth" ]; then
    echo "⚠️ Warning: Model file not found at model/resnet_Model.pth"
    echo "   Please ensure the trained model is in the correct location"
fi

echo "✅ Setup complete!"
echo ""
echo "🚀 To start the application:"
echo "   source venv/bin/activate"
echo "   streamlit run src/app.py"
echo ""
echo "🐳 To run with Docker:"
echo "   docker-compose up --build"
echo ""
echo "🧪 To run tests:"
echo "   python -m pytest tests/"
