import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from firebase_setup import save_report
import random
import time

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
st.subheader("Empowering Safer Online Spaces with AI")

st.write(""" 
SafeSpace is a tool designed to help identify and address online harassment targeting women and girls. 
Using advanced AI, SafeSpace analyzes text to determine whether it contains harmful or abusive content. 
This empowers users to navigate online interactions with increased confidence and safety.
""")

# How to use the tool
st.markdown("### How to Use SafeSpace")
st.write(""" 
1. Enter a message in the **Message** field below.
2. Click the **Detect** button to check if the message contains harassment.
3. View the results to see if the message is classified as "Safe" or "Harassment" along with the confidence score.
4. If harassment is detected, SafeSpace will provide safety tips to help you respond.
""")

# Sample text suggestions
st.markdown("#### Sample Messages to Try")
st.write(""" 
- "You are so inspiring. Keep up the great work!"
- "Everyone thinks you're terrible. Just leave already."
- "Thank you for your help on the project."
- "You don't deserve to be here."
""")

# User input section
st.markdown("### Analyze a Message")
user_input = st.text_area("Enter a message you want to check:", "")

# Detect button and output display
if st.button("Detect"):
    if user_input:
        # Show spinner while processing
        with st.spinner("Analyzing... 🧐"):
            time.sleep(2)  # Mimic processing delay
        
        # Run classification
        label, confidence = classify_text(user_input)

        # Display result as button
        if label == "Harassment":
            st.markdown("""
                <style>
                    .result-btn-harassment {
                        background-color: red;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 5px;
                        text-align: center;
                        font-size: 18px;
                        font-weight: bold;
                        cursor: not-allowed;
                        border: none;
                    }
                </style>
                <button class="result-btn-harassment" disabled>🚫 Harassment Detected - Confidence: {:.2f}</button>
            """.format(confidence), unsafe_allow_html=True)
            
            tips = [
                "Consider blocking or reporting the user if the harassment persists.",
                "Seek support from a trusted friend or family member.",
                "Practice online safety and protect your personal information."
            ]
            st.warning("**Safety Tip:** " + random.choice(tips))
        else:
            st.markdown("""
                <style>
                    .result-btn-safe {
                        background-color: green;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 5px;
                        text-align: center;
                        font-size: 18px;
                        font-weight: bold;
                        cursor: not-allowed;
                        border: none;
                    }
                </style>
                <button class="result-btn-safe" disabled>✅ Message is Safe - Confidence: {:.2f}</button>
            """.format(confidence), unsafe_allow_html=True)

        # Save report to Firebase
        user_id = "zMRSBNz5AygIReNXxfVxwJkaEA32"
        save_report(user_id, user_input, label, float(confidence))

    else:
        st.error("Please enter some text to analyze.")
