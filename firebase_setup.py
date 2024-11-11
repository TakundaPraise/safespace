import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, auth
from google.api_core.exceptions import GoogleAPIError

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variable
google_credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Print the credentials path for verification (remove or comment this in production)
print(f"Credentials Path: {google_credentials_path}")

# Initialize Firebase app only if it hasn't been initialized yet
if not firebase_admin._apps:
    cred = credentials.Certificate(google_credentials_path)
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# User registration (mockup function)
def register_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print(f"Successfully registered user: {user.uid}")
        return user
    except Exception as e:
        print(f"Error registering user: {e}")
        return None

# Save harassment reports
from google.cloud import firestore

# Firestore database instance
db = firestore.client()

# Save harassment reports
def save_report(user_id, user_input, label, confidence):
    try:
        # Add a new document to the "reports" collection with the specified fields
        db.collection("reports").add({
            "user_id": user_id,
            "input": user_input,
            "label": label,
            "confidence": confidence,
            "timestamp": firestore.SERVER_TIMESTAMP  # Automatically set the current timestamp
        })
        print("Report saved to Firestore.")
    except Exception as e:
        print(f"Error saving report to Firestore: {e}")

