import streamlit as st
import requests
from PIL import Image
import io

# Streamlit UI
st.title("Coffee Bean Classification")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Predict"):
        # Convert image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="JPEG")
        img_bytes = img_bytes.getvalue()

        # Send to API
        st.write("Predicting...")
        response = requests.post("https://deployment-yhub.onrender.com/predict", files={"file": img_bytes})


        
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"Prediction: **{prediction}**")
        else:
            st.error("Error in prediction.")
