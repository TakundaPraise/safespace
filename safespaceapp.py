import streamlit as st
import requests
from firebase_setup import save_report
import random
import time

# Load Google Gemini Model (modify this function as needed for Google Gemini)
def classify_text_with_gemini_api(text):
    # Example endpoint and headers (replace with actual API details)
    url = "https://gemini.googleapis.com/v1/models/170508869017:predict"
    headers = {
        "Authorization": "Bearer AIzaSyDUFgiGiQz1gnlTAtMig59xZBs17N-jQ2w",
        "Content-Type": "application/json"
    }
    data = {
        "instances": [text]
    }
    
    # Make API request
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    # Extract label and confidence from response (adapt this based on actual Gemini API response)
    if response.status_code == 200:
        scores = response_data["predictions"][0]["scores"]
        label = "Harassment" if scores[1] > 0.5 else "Safe"
        confidence = scores[1] if label == "Harassment" else scores[0]
        return label, confidence
    else:
        st.error("Error: Unable to connect to Google Gemini API.")
        return None, None

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
        label, confidence = classify_text_with_gemini_api(user_input)

        # Display result if the classification is successful
        if label and confidence:
            st.markdown("### Results")
            st.write(f"**Classification:** {label}")
            st.write(f"**Confidence Level:** {confidence:.2f}")

            # Convert confidence to native float before saving to Firebase
            confidence = float(confidence)

            # Mock user authentication (in production, connect with Firebase Auth)
            user_id = "zMRSBNz5AygIReNXxfVxwJkaEA32"

            # Save report to Firebase
            save_report(user_id, user_input, label, confidence)

            # Show custom buttons based on the result
            if label == "Harassment":
                st.markdown("""
                    <style>
                        .harassment-btn {
                            background-color: red;
                            color: white;
                            padding: 10px 20px;
                            border-radius: 5px;
                            text-align: center;
                            font-size: 18px;
                            cursor: pointer;
                        }
                    </style>
                    <button class="harassment-btn" disabled>🚫 Harassment Detected</button>
                """, unsafe_allow_html=True)
                
                tips = [
                    "Consider blocking or reporting the user if the harassment persists.",
                    "Seek support from a trusted friend or family member.",
                    "Practice online safety and protect your personal information."
                ]
                st.warning("**Safety Tip:** " + random.choice(tips))
            else:
                st.markdown("""
                    <style>
                        .safe-btn {
                            background-color: green;
                            color: white;
                            padding: 10px 20px;
                            border-radius: 5px;
                            text-align: center;
                            font-size: 18px;
                            cursor: pointer;
                        }
                    </style>
                    <button class="safe-btn" disabled>✅ Message is Safe</button>
                """, unsafe_allow_html=True)

    else:
        st.error("Please enter some text to analyze.")
