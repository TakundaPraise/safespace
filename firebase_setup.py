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
def save_report(user_id, user_input, label, confidence):
    try:
        report_data = {
            "user_id": user_id,
            "input": user_input,
            "label": label,
            "confidence": confidence,
            "timestamp": firestore.SERVER_TIMESTAMP  # Optional: adds a timestamp to the report
        }
        # Add the document to Firestore
        db.collection("reports").add(report_data)
        print("Report successfully saved.")
    except GoogleAPIError as e:
        print(f"Error saving report to Firestore: {e}")
