import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image


st.set_page_config(page_title="Pet Image Classifier", layout="centered")

st.title("🐾 Pet Expression Classifier")
st.write("Upload an image of a pet, and the model will classify it as Happy, Sad or Angry!")

try:
    model_path = 'Pet_Expression_Classifier.keras'
    model = load_model(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

data_cat = ['Angry', 'Other', 'Sad', 'happy']

st.header("Upload an Image")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:

        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        img_height, img_width = 180, 180
        image = Image.open(uploaded_file)
        image_resized = image.resize((img_width, img_height))
        img_array = np.expand_dims(np.array(image_resized) / 255.0, axis=0)

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        st.subheader("Prediction Results")
        predicted_class = data_cat[np.argmax(score)]
        confidence = np.max(score) * 100
        st.success(f"The pet in the image is **{predicted_class}**.")
        st.info(f"Confidence Level: **{confidence:.2f}%**")
    except Exception as e:
        st.error(f"Error processing the image: {e}")
else:
    st.info("Please upload an image to get started!")


st.markdown(
    """
    ---
    *Project by Sushant*
    """
)
