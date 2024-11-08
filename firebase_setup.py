# firebase_setup.py (Run this once to initialize Firebase in your project)

import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Firebase app
cred = credentials.Certificate("config/firebase-adminsdk.json")  # Add your Firebase credentials
firebase_admin.initialize_app(cred)

db = firestore.client()

# User registration (mockup)
def register_user(email, password):
    user = auth.create_user(email=email, password=password)
    return user

# Save harassment reports
def save_report(user_id, text, label, confidence):
        # Convert confidence to a native Python float
    confidence = float(confidence)
    db.collection("reports").add({
        "user_id": user_id,
        "text": text,
        "label": label,
        "confidence": confidence
    })


