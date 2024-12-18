import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np

# Load the trained MobileNetV2 model
model = load_model('apple_classifier_sequential.keras')

# Define the class names
class_names = ["Apple_scab", "Apple_Black_rot", "Cedar_Apple", "Healthy"]

# Streamlit App Title
st.title("Apple Leaf Disease Classification")
st.write("Upload an image to classify it into one of the disease categories.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.write("Your prediction will be shown below...")

    # Preprocess the image
    img = load_img(uploaded_file, target_size=(224, 224))  # Resize to MobileNet input size
    img_array = img_to_array(img)  # Convert to array
    img_array = preprocess_input(img_array)  # Preprocess the image (scales to [-1, 1])
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict
    predictions = model.predict(img_array)[0]  # Get predictions
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # Highlight the maximum prediction
    st.write(f"### Predicted Class: {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}%")

    # Display progress bars for each class
    st.write("### Class Confidence:")
    for i, class_name in enumerate(class_names):
        st.write(f"{class_name}: {predictions[i] * 100:.2f}%")
        st.progress(int(predictions[i] * 100))  # Show progress as percentage
