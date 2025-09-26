@echo off
REM Rice Disease Prediction Setup Script for Windows
REM This script sets up the development environment

echo 🌾 Setting up Rice Disease Prediction System...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.9+ first.
    pause
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
echo 📁 Creating directories...
if not exist "static\images" mkdir static\images
if not exist "static\uploads" mkdir static\uploads
if not exist "tests" mkdir tests
if not exist "docs" mkdir docs

REM Copy images if they exist
if exist "image" (
    echo 🖼️ Copying images...
    xcopy /E /I /Y image\* static\images\
)

if exist "uploads" (
    echo 📤 Copying uploads...
    xcopy /E /I /Y uploads\* static\uploads\
)

REM Create .gitkeep files
echo. > static\uploads\.gitkeep

REM Check if model file exists
if not exist "model\resnet_Model.pth" (
    echo ⚠️ Warning: Model file not found at model\resnet_Model.pth
    echo    Please ensure the trained model is in the correct location
)

echo ✅ Setup complete!
echo.
echo 🚀 To start the application:
echo    venv\Scripts\activate
echo    streamlit run src\app.py
echo.
echo 🐳 To run with Docker:
echo    docker-compose up --build
echo.
echo 🧪 To run tests:
echo    python -m pytest tests\

pause
