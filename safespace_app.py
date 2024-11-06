# safespace_app.py

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from firebase_setup import save_report
import random

# Load model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    return tokenizer, model

tokenizer, model = load_model()

# Function to classify text
def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    scores = torch.softmax(outputs.logits, dim=1).detach().cpu().numpy()
    label = "Harassment" if scores[0][1] > 0.5 else "Safe"
    confidence = scores[0][1] if label == "Harassment" else scores[0][0]
    return label, confidence

# Streamlit app UI
st.title("SafeSpace - Online Harassment Detector for Women and Girls")
st.write("Check if a message contains harmful or abusive content.")

# User input
user_input = st.text_area("Message", "")
if st.button("Detect"):
    if user_input:
        label, confidence = classify_text(user_input)
        st.write(f"**Result:** {label}")
        st.write(f"**Confidence:** {confidence:.2f}")

        # Mock user authentication (in production, connect with Firebase Auth)
        user_id = "example_user_id"

        # Save report to Firebase
        save_report(user_id, user_input, label, confidence)

        # Provide helpful tips based on the classification result
        if label == "Harassment":
            tips = [
                "Consider blocking or reporting the user if the harassment persists.",
                "Seek support from a trusted friend or family member.",
                "Practice online safety and protect your personal information."
            ]
            st.write("**Safety Tip:** " + random.choice(tips))
    else:
        st.write("Please enter some text to analyze.")
