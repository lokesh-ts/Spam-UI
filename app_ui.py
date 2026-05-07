import streamlit as st
import requests

# UI Title
st.title("📩 Spam Classifier App")

st.write("Enter a message and check if it's spam or not")

# Input box
text = st.text_area("Message")

# IMPORTANT: replace with your Render URL
API_URL = "https://spam-classifier-api-3hos.onrender.com/predict"

# Button
if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a message")
    else:
        response = requests.post(
            API_URL,
            json={"text": text}
        )

        if response.status_code == 200:
            result = response.json()

            st.subheader("Result")
            st.write("Prediction:", result["label"])
        else:
            st.error("API Error. Check backend deployment.")