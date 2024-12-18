# 🍎 Apple Disease Detection using MobileNet

This project is a web-based application for detecting apple diseases using a pre-trained **MobileNet** model. It allows users to upload apple images and classify them into one of five categories. The application is deployed using **Streamlit Community Cloud** for easy access.

---

## 📋 Features
- **Disease Classification**: Detects apple diseases and classifies them into:
  - Apple Scab
  - Apple Black rot
  - Apple cedar
  - Healthy
- **Interactive Web Interface**: Upload images and get real-time predictions with confidence scores.
- **MobileNet Backbone**: Powered by a lightweight and efficient MobileNet model.
- **Deployed on Streamlit**: Accessible from anywhere without requiring local installation.

---

## 🌐 Deployment
The application is live on **Streamlit Community Cloud**.  
🔗 **Access the App**: [Apple Disease Detection](https://applediseasedetectionsk.streamlit.app/)

---

## 🛠️ How to Run Locally
### 1. Prerequisites
- Python 3.8 or higher
- `pip` for dependency management

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/apple-disease-detection.git
cd apple-disease-detection
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Streamlit App
bash
Copy code
streamlit run app.py
5. Access the App
Open your browser and navigate to http://localhost:8501.
```
### 📂 Directory Structure
bash
Copy code
apple-disease-detection/
├── app.py                # Streamlit app script
├── mobilenet_model.h5    # Pre-trained MobileNet model
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
### 🤖 How It Works
Upload an image of an apple using the interface.
The application preprocesses the image to match MobileNet's input requirements.
The model predicts the category of the image.
Results are displayed along with the confidence score.
### 🖼️ Sample Output
Input Image	Predicted Class	Confidence Score
Disease 1	95%
### Model Performance
Train Accuracy: 1.0000
Validation Accuracy: 1.0000
Train Loss: 0.0118
Validation Loss: 0.0067
Generalization:
The model is performing well with excellent accuracy on both the training and validation datasets, and it generalizes effectively to unseen data.

### 🧾 Dependencies
The application requires the following Python packages:

streamlit
tensorflow
numpy
pillow
Refer to the requirements.txt file for a full list of dependencies.

