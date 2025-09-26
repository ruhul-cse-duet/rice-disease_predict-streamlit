"""
Main Streamlit application for Rice Disease Prediction
"""
import streamlit as st
import pandas as pd
import time
import logging
from PIL import Image
from typing import Optional

# Import custom modules
from models.resnet_model import RiceDiseasePredictor
from services.treatment_service import TreatmentService
from utils.device_utils import get_device
from utils.image_utils import preprocess_image, validate_image, display_image_info
from config.settings import (
    CLASS_NAMES, 
    STREAMLIT_CONFIG, 
    IMAGE_CONFIG,
    LOGGING_CONFIG
)

# Configure logging
logging.basicConfig(**LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Configure Streamlit page
st.set_page_config(**STREAMLIT_CONFIG)

class RiceDiseaseApp:
    """Main application class for Rice Disease Prediction"""
    
    def __init__(self):
        self.device = get_device()
        self.predictor = None
        self.treatment_service = TreatmentService()
        self._load_model()
    
    def _load_model(self):
        """Load the prediction model"""
        try:
            self.predictor = RiceDiseasePredictor(device=self.device)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            st.error("Error loading the prediction model. Please check the model file.")
    
    def render_home_page(self):
        """Render the home page"""
        st.markdown('<h2 style="color:#DB3614;">RICE DISEASE RECOGNITION & TREATMENT MANAGEMENT</h2>',
                   unsafe_allow_html=True)
        
        # Display main image
        try:
            image_path = 'static/images/4.png'
            st.image(image_path, width=850)
        except FileNotFoundError:
            st.info("Main image not found. Please ensure images are in the static/images directory.")
        
        st.markdown("##")
        
        st.markdown('<h2 style="color:red;"> Welcome Our RICE Disease Recognition Apps! 🌿🔍</h2>', 
                   unsafe_allow_html=True)
        st.markdown("""
            Our mission is to help in identifying plant diseases efficiently. 
            Upload an image of a plant, and our system will analyze it to detect any signs of diseases. 
            Together, let's protect our crops and ensure a healthier harvest!
        """)
        
        st.markdown('<h3 style="color:#A52A2A;"> How Predict The Rice Disease follow the Procedure</h3>', 
                   unsafe_allow_html=True)
        st.markdown("""
        1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
        2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
        3. **Results:** View the results and recommendations for further action.
        """)
        
        # Display prediction process image
        try:
            img_path = 'static/images/predict.png'
            st.image(img_path, caption="Prediction Process for Rice Disease", width=800)
        except FileNotFoundError:
            st.info("Prediction process image not found.")
        
        st.markdown("###")
        
        st.markdown('<h3 style="color:#A52A2A;"> Why Choose Us?</h3>', unsafe_allow_html=True)
        st.markdown("""
        - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
        - **User-Friendly:** Simple and intuitive interface for seamless user experience.
        - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.
        """)
        
        # Display disease types image
        try:
            img_path = 'static/images/Types-of-rice-leaf-disease-RLD.png'
            st.image(img_path, width=800)
        except FileNotFoundError:
            st.info("Disease types image not found.")
        
        st.markdown('<h3 style="color:#A52A2A;"> Get Started </h3>', unsafe_allow_html=True)
        st.markdown("""
            Click on the **Disease Recognition** page in the sidebar to upload an image and experience the
            power of our Rice Disease Recognition System! """)
        
        st.markdown('<h3 style="color:#A52A2A;"> About Us </h3>', unsafe_allow_html=True)
        st.markdown("""
        Learn more about the project, our team, and our goals on the **About** page.
        """)
    
    def render_about_page(self):
        """Render the about page"""
        st.markdown('<h2 style="color:yellow;">About Our Project </h2>', unsafe_allow_html=True)
        
        # Display about image
        try:
            img_path = 'static/images/3.png'
            st.image(img_path, width=800)
        except FileNotFoundError:
            st.info("About image not found.")
        
        st.markdown('<h3 style="color:yellow;"> Dataset Overview – Rice Disease Prediction </h3>', 
                   unsafe_allow_html=True)
        st.markdown("""
            Our Rice Disease Prediction project utilizes a high-quality dataset consisting of 11,790 images.
            These images are categorized into 9 distinct classes, covering both diseased and healthy rice leaves.
            The dataset is split into 85% training and 15% validation sets to ensure balanced model learning.
            Each category includes diverse samples to improve the model's robustness and generalization.
            This dataset enables our deep learning model to detect rice diseases with high accuracy.
            It plays a vital role in providing farmers with quick and reliable diagnostics.
        """)
        
        st.markdown("""
            - **Train (10000 images)**
            - **Test (3422 images)**
            - **validation (1770 images)**
            - **Image size : 224x224**
        """)
        
        # Create structured data for table
        data = []
        for cls in CLASS_NAMES:
            data.append({"ফসলের নাম (Crops)": 'Rice', "রোগ/অবস্থা (Condition)": cls})
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        st.markdown(
            "<h3 style='text-align: center; color: yellow;'>🌿 List of Rice Crops with Disease</h3>",
            unsafe_allow_html=True
        )
        st.dataframe(df, use_container_width=True)
        
        st.markdown('<h3 style="color:#FFA500;"> Model Architecture --CNN + Custom ResNet</h3>', 
                   unsafe_allow_html=True)
        st.markdown("""
        The **Rice Disease Prediction** project employs a hybrid deep learning architecture combining 
        **Convolutional Neural Networks (CNN)** with a **customized ResNet (Residual Network)**.  

        This approach leverages CNN's ability to extract spatial features and ResNet's strength in handling deep architectures through 
        *skip connections*, minimizing vanishing gradient issues.

        📐 **Input Size:** 224 × 224 pixels – optimized for consistent layer performance.

        🔧 **Customization:** Our ResNet includes modified convolutional and residual blocks specially tailored for agricultural image data.

        ⚙️ This fusion allows the model to learn complex patterns and detect diseases with greater **accuracy** and **reliability**.

        🚀 The system remains **lightweight** yet powerful enough for **real-time predictions**.
        """)
        
        # Display architecture image
        try:
            img = Image.open('static/images/Rice-leaf-disease-identification-by-ResNet34.png')
            st.image(img, caption="CNN + Custom ResNet Architecture for Rice Disease Prediction", width=800)
        except FileNotFoundError:
            st.info("Architecture image not found.")
    
    def render_prediction_page(self):
        """Render the disease recognition page"""
        st.markdown('<h2 style="color:#FFA500;"> Rice Disease Recognition</h2>', 
                   unsafe_allow_html=True)
        
        # File uploader
        test_image = st.file_uploader(
            "Upload an image", 
            type=IMAGE_CONFIG['allowed_formats'],
            help=f"Supported formats: {', '.join(IMAGE_CONFIG['allowed_formats'])}"
        )
        
        if test_image is not None:
            try:
                # Load and process image
                image = Image.open(test_image).convert("RGB")
                
                # Validate image
                if not validate_image(image):
                    st.error("Image is too small or too large. Please upload a valid image.")
                    return
                
                # Display image info
                with st.expander("Image Information"):
                    display_image_info(image)
                
                # Display uploaded image
                st.image(image, caption="Uploaded image", width=400)
                
                # Preprocess image
                processed_image = preprocess_image(image)
                
                # Prediction button
                if st.button("Predict", type="primary"):
                    if self.predictor is None:
                        st.error("Model not loaded. Please check the model file.")
                        return
                    
                    st.snow()
                    st.write("Our Disease Prediction Result : ")
                    
                    start_time = time.time()
                    
                    try:
                        # Make prediction
                        result = self.predictor.predict(processed_image)
                        
                        # Display result
                        st.success(f"Predicted Class is --->  {CLASS_NAMES[result]}")
                        
                        # Display treatment recommendation
                        self.treatment_service.display_treatment(CLASS_NAMES[result])
                        
                        end_time = time.time()
                        prediction_time = end_time - start_time
                        logger.info(f"Prediction Response Time: {prediction_time:.4f} sec")
                        
                        # Display performance metrics
                        st.info(f"Prediction completed in {prediction_time:.2f} seconds")
                        
                    except Exception as e:
                        logger.error(f"Prediction error: {e}")
                        st.error(f"Error during prediction: {e}")
                        
            except Exception as e:
                logger.error(f"Image processing error: {e}")
                st.error(f"Error processing image: {e}")
        else:
            st.warning("Please upload an image file to continue.")
    
    def run(self):
        """Run the main application"""
        # Sidebar
        st.sidebar.title("Menu-bar")
        app_mode = st.sidebar.selectbox("Select the Page", ["HOME", "About", "Disease Recognition"])
        
        # Render appropriate page
        if app_mode == "HOME":
            self.render_home_page()
        elif app_mode == "About":
            self.render_about_page()
        elif app_mode == "Disease Recognition":
            self.render_prediction_page()

def main():
    """Main function to run the application"""
    app = RiceDiseaseApp()
    app.run()

if __name__ == "__main__":
    main()

# streamlit run src/app.py