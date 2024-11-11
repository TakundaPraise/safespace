# firebase_setup.py (Run this once to initialize Firebase in your project)

import firebase_admin
from firebase_admin import credentials, firestore, auth

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

