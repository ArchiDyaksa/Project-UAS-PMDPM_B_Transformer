import streamlit as st
from streamlit_extras.let_it_rain import rain
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import base64
from pathlib import Path
from st_social_media_links import SocialMediaIcons

# Load the pre-trained model
# Load the pre-trained model
model_path = 'BestModel_MOBILENET_Transformer.h5'  # Update with your model path
class_names = ['Busuk', 'Matang', 'Mentah']

# Function to preprocess and classify image
def classify_image(image_path):
    try:
        # Load and preprocess the image
        input_image = tf.keras.utils.load_img(image_path, target_size=(180, 180))
        input_image_array = tf.keras.utils.img_to_array(input_image)
        input_image_exp_dim = tf.expand_dims(input_image_array, 0)

        # Predict using the model
        predictions = model.predict(input_image_exp_dim)
        result = tf.nn.softmax(predictions[0])  # Apply softmax for probability
        
        # Get class with highest confidence
        class_idx = np.argmax(result)
        confidence_scores = result.numpy()
        return class_names[class_idx], confidence_scores
    except Exception as e:
        return "Error", str(e)

# Function to create a custom progress bar
def custom_progress_bar(confidence, color1, color2, color3):
    percentage1 = confidence[0] * 100  # Confidence for class 0 (Busuk)
    percentage2 = confidence[1] * 100  # Confidence for class 1 (Matang)
    percentage3 = confidence[2] * 100  # Confidence for class 2 (Mentah)
    progress_html = f"""
    <div style="border: 1px solid #ddd; border-radius: 5px; overflow: hidden; width: 100%; font-size: 14px;">
        <div style="width: {percentage1:.2f}%; background: {color1}; color: white; text-align: center; height: 24px; float: left;">
            {percentage1:.2f}% Busuk
        </div>
        <div style="width: {percentage2:.2f}%; background: {color2}; color: black; text-align: center; height: 24px; float: left;">
            {percentage2:.2f}% Matang
        </div>
        <div style="width: {percentage3:.2f}%; background: {color3}; color: black; text-align: center; height: 24px; float: left;">
            {percentage3:.2f}% Mentah
        </div>
    </div>
    """
    st.sidebar.markdown(progress_html, unsafe_allow_html=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
# Function to apply Fire effect
def run_fire_animation():
    rain(emoji="🍌", font_size=40, falling_speed=10, animation_length="infinite")

# Run fire animation
run_fire_animation()

# Change Background Streamlit
set_background(r"background1.gif")

# Add custom background with snow animation
background = """
<style>
/* Set full-page background */
# [data-testid="stAppViewContainer"] {
#     background: linear-gradient(to bottom, #FF0000, #00FF00); /* Red to Green */
#     background-size: cover;
#     background-attachment: fixed;
#     color: white; /* Text color */
#     font-family: Arial, sans-serif;
# }

/* Hide default Streamlit styling for a cleaner look */
[data-testid="stSidebar"] {
    background: #fbb99f;
    color: white;
}

/* Perbaiki warna teks judul agar tetap terlihat */
h1, h2, h3, h4, h5, h6, p {
    color: white; 
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8); /* Efek bayangan */
}

/* Create fire animation */
.fire {
    color: #red;
    font-size: 1.5em;
    position: absolute;
    top: -10%;
    animation: fire 10s linear infinite;
    opacity: 0.8;
    z-index: 10;
}

@keyframes fire {
    0% { transform: translateY(0); }
    100% { transform: translateY(100vh); }
}

.fire:nth-child(1) { left: 10%; animation-delay: 0s; }
.fire:nth-child(2) { left: 20%; animation-delay: 2s; }
.fire:nth-child(3) { left: 30%; animation-delay: 4s; }
.fire:nth-child(4) { left: 40%; animation-delay: 6s; }
.fire:nth-child(5) { left: 50%; animation-delay: 8s; }
.fire:nth-child(6) { left: 60%; animation-delay: 1s; }
.fire:nth-child(7) { left: 70%; animation-delay: 3s; }
.fire:nth-child(8) { left: 80%; animation-delay: 5s; }
.fire:nth-child(9) { left: 90%; animation-delay: 7s; }
.fire:nth-child(10) { left: 100%; animation-delay: 9s; }
</style>
"""

# Display the background animation and fire
st.markdown(background, unsafe_allow_html=True)

title_html = """
<div style="text-align: center; color: #fbb99f; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8); font-size: 50px; font-weight: bold;">
    🍌 Prediksi Kematangan Buah Pisang - Transformer 🍌
</div>
"""
st.markdown(title_html, unsafe_allow_html=True)

file_uploader_style = """
<style>
/* Tambahkan padding untuk memperbesar area komponen */
div[data-testid="stFileUploader"] {
    margin-top: 20px;
    margin-bottom: 20px;
    padding: 20px;
    border: 2px dashed #FF4500; /* Tambahkan border dengan warna */
    border-radius: 10px; /* Border radius untuk sudut melengkung */
    background-color: #fbb99f; /* Warna latar belakang (peach puff) */
}
</style>
"""

# Terapkan styling ke file uploader
st.markdown(file_uploader_style, unsafe_allow_html=True)

# Upload multiple files in the main page
uploaded_files = st.file_uploader(
    "Unggah Gambar (Beberapa diperbolehkan)", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.sidebar.image(image, caption=f"{uploaded_file.name}", use_container_width=True)
    
# Style for the prediction button
style_button = """
<style>
.button-prediksi {
    display: block;
    margin: 0 auto;
    text-align: center;
}
</style>
"""
st.markdown(style_button, unsafe_allow_html=True)

# Sidebar for prediction button and results
col1, col2, col3 = st.sidebar.columns([1, 1, 1])
with col2:
    if st.button("Prediksi"):
        st.snow()
        if uploaded_files:
            st.sidebar.write("### 🎁 Hasil Prediksi")
            with st.spinner('Memprediksi...'):
                for uploaded_file in uploaded_files:
                    with open(uploaded_file.name, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    # Perform prediction
                    label, confidence = classify_image(uploaded_file.name)
                    
                    if label != "Error":
                        # Define colors for the bar and label
                        primary_color = "#000000"  # Black for "Busuk"
                        secondary_color = "#FFFF00"  # Yellow for "Matang"
                        tertiary_color = "00FF00"  # Green for "Mentah"
                        
                        if label == "Busuk":
                            label_color = primary_color
                        elif label == "Matang":
                            label_color = secondary_color
                        elif label == "Mentah":
                            label_color = tertiary_color
                        
                        # Display prediction results
                        st.sidebar.write(f"**Nama File:** {uploaded_file.name}")
                        st.sidebar.markdown(f"<h4 style='color: {label_color};'>Prediksi: {label}</h4>", unsafe_allow_html=True)
                        
                        # Display confidence scores
                        st.sidebar.write("**Confidence:**")
                        for i, class_name in enumerate(class_names):
                            st.sidebar.write(f"- {class_name}: {confidence[i] * 100:.2f}%")
                        
                        # Display custom progress bar
                        custom_progress_bar(confidence, primary_color, secondary_color, tertiary_color)
                        
                        st.sidebar.write("---")
                    else:
                        st.sidebar.error(f"Kesalahan saat memproses gambar {uploaded_file.name}: {confidence}")
        else:
            st.sidebar.error("Silakan unggah setidaknya satu gambar untuk diprediksi.")

# Preview images in the main page
if uploaded_files:
    st.write("### Preview Gambar")
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"{uploaded_file.name}", use_container_width=True)
        
# Tambahkan copyright di bagian bawah
copyright_html = """
<div style="text-align: center; margin-top: 5px; font-size: 20px; font-wight: bold; color: black; opacity: 1;">
    © 2024 Transformer. All Rights Reserved. <br>
    Frans Daniel Rajagukguk / 220711826 <br>
    Angello Khara Sitanggang / 220711833 <br>
    Davin Gilbert Natanael / 220711841 <br>
    Emanuel Enrico Anindya Wibawa / 220711890 <br>
    Archipera Rari Dyaksa / 220711891 <br>
</div>
"""
st.markdown(copyright_html, unsafe_allow_html=True)

main_social_media_html = """
<div style="text-align: center; margin-top: 10px;">
    <a href="https://github.com/ArchiDyaksa/Project-UAS-PMDPM_B_Transformer" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="width: 40px; margin: 10px;">
    </a>
    <a href="https://youtu.be/dQw4w9WgXcQ?si=xq0SADs2r9-txQOj" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width: 40px; margin: 10px;">
    </a>
</div>
"""
st.markdown(main_social_media_html, unsafe_allow_html=True)
