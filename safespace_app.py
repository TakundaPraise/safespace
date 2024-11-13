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

# Define supported African languages in Southern Africa with respective translation models
southern_african_language_models = {
    "sw": "Helsinki-NLP/opus-mt-sw-en",  # Swahili to English
    "zu": "Helsinki-NLP/opus-mt-zu-en",  # Zulu to English
    # Currently no specific models for Shona, Ndebele, or Xhosa
}

# Load main classification model
@st.cache_resource
def load_classification_model():
    tokenizer_classify = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    model_classify = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    return tokenizer_classify, model_classify

# Load translation models dynamically
@st.cache_resource
def load_translation_model(language_code):
    if language_code in southern_african_language_models:
        model_translate = MarianMTModel.from_pretrained(southern_african_language_models[language_code])
        tokenizer_translate = MarianTokenizer.from_pretrained(southern_african_language_models[language_code])
        return model_translate, tokenizer_translate
    else:
        return None, None

tokenizer_classify, model_classify = load_classification_model()

# Function to translate text to English
def translate_to_english(text, language_code):
    model_translate, tokenizer_translate = load_translation_model(language_code)
    if model_translate and tokenizer_translate:
        inputs = tokenizer_translate(text, return_tensors="pt", truncation=True)
        translated = model_translate.generate(**inputs)
        return tokenizer_translate.decode(translated[0], skip_special_tokens=True)
    else:
        return None

# Function to classify text
def classify_text(text):
    try:
        # Detect language
        language = detect(text)
        
        # Check if translation is required
        if language != "en" and language in southern_african_language_models:
            translated_text = translate_to_english(text, language)
            if translated_text:
                text = translated_text  # Use translated text for classification
            else:
                st.warning(f"Translation for {language} is currently unsupported. Text will be analyzed as-is.")
                # Classify text (in English or untranslated)
        inputs = tokenizer_classify(text, return_tensors="pt")
        outputs = model_classify(**inputs)
        scores = torch.softmax(outputs.logits, dim=1).detach().cpu().numpy()
        label = "Harassment" if scores[0][1] > 0.5 else "Safe"
        confidence = scores[0][1] if label == "Harassment" else scores[0][0]
        return label, confidence
    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")
        return "Error", 0.0






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

        # Display result
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
