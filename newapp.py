import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, MarianMTModel, MarianTokenizer
from langdetect import detect
import torch
from firebase_setup import save_report
import random
import time

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

# Streamlit UI
st.title("SafeSpace - Online Harassment Detector for Women and Girls")
st.subheader("Empowering Safer Online Spaces with AI")

st.markdown("### Analyze a Message")
user_input = st.text_area("Enter a message you want to check:", "")

# Detect button and output display
if st.button("Detect"):
    if user_input:
        with st.spinner("Analyzing... 🧐"):
            time.sleep(2)  # Mimic processing delay

        # Run classification
        label, confidence = classify_text(user_input)

        # Display result
        st.markdown("### Results")
        if label == "Error":
            st.error("Unable to process the input message.")
        else:
            st.write(f"**Classification:** {label}")
            st.write(f"**Confidence Level:** {confidence:.2f}")

            # Save report to Firebase
            user_id = "zMRSBNz5AygIReNXxfVxwJkaEA32"
            save_report(user_id, user_input, label, float(confidence))

            # Display buttons based on result
            if label == "Harassment":
                st.markdown("""
                    <button style="background-color: red; color: white; padding: 10px 20px; border-radius: 5px; font-size: 18px; cursor: not-allowed;">🚫 Harassment Detected</button>
                """, unsafe_allow_html=True)
                st.warning("**Safety Tip:** " + random.choice([
                    "Consider blocking or reporting the user.",
                    "Seek support from trusted friends or family.",
                    "Stay safe and protect personal information."
                ]))
            else:
                st.markdown("""
                    <button style="background-color: green; color: white; padding: 10px 20px; border-radius: 5px; font-size: 18px; cursor: not-allowed;">✅ Message is Safe</button>
                """, unsafe_allow_html=True)
    else:
        st.error("Please enter some text to analyze.")
