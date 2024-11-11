# firebase_setup.py (Run this once to initialize Firebase in your project)
import google
from google.api_core.exceptions import GoogleAPIError
from google.cloud import firestore

import firebase_admin
from firebase_admin import credentials, firestore, auth

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variable (e.g., GOOGLE_APPLICATION_CREDENTIALS)
google_credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Now you can use google_credentials_path or any other secrets in your app
print(f"Credentials Path: {google_credentials_path}")


# Initialize Firebase app
cred = credentials.Certificate("config/firebase-adminsdk.json")  # Add your Firebase credentials
firebase_admin.initialize_app(cred)

db = firestore.client()

# User registration (mockup)
def register_user(email, password):
    user = auth.create_user(email=takundapraiseg@gmail.com, password=12345678)
    return user

# Save harassment reports
def save_report(user_id, user_input, label, confidence):
    try:
        db.collection("reports").add({
            "user_id": user_id,
            "input": user_input,
            "label": label,
            "confidence": confidence,
        })
    except google.api_core.exceptions.GoogleAPIError as e:
        print(f"Error saving report to Firestore: {e}")

