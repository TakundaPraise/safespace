SafeSpace is an AI tool developed to help women and girls recognize and respond to online harassment. By using the cardiffnlp/twitter-roberta-base-offensive model, the tool evaluates messages for potentially harmful content and classifies them as either "Harassment" or "Safe." Firebase integration enables user authentication and stores reports for further analysis, ensuring data security. The tool empowers women to stand up to online harassment, offering safety resources and providing support. By leveraging AI, SafeSpace works towards gender equality by making it easier for women and girls to safely engage with online spaces, thereby reducing the gender disparities present in digital interactions.

Testing Instructions for SafeSpace Application
your GitHub repository.

markdown
Copy code
# SafeSpace - Online Harassment Detector for Women and Girls

## Overview
SafeSpace is a tool designed to help women and girls identify and address online harassment. Using the **cardiffnlp/twitter-roberta-base-offensive** model, SafeSpace analyzes messages to classify them as either "Harassment" or "Safe". It integrates with Firebase to store reports for further analysis, ensuring data security and empowering users to take action when necessary.

## Prerequisites

Before you begin, ensure that you have the following installed on your machine:

- Python 3.x
- Streamlit
- Transformers
- Torch
- Firebase Admin SDK
- Google Cloud Firestore
- dotenv (for managing environment variables)

To install the required dependencies, run:

```bash
pip install streamlit transformers torch firebase-admin google-cloud-firestore python-dotenv
Setting Up the Environment
Clone the repository: First, clone the SafeSpace repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/safespace.git
cd safespace
Set up Firebase:

Create a Firebase project at Firebase Console.

Download the Firebase Admin SDK credentials file and save it as firebase-adminsdk.json in your project folder.

Add the Firebase credentials to your environment variables by creating a .env file in the root of your project and adding the following:

bash
Copy code
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/firebase-adminsdk.json
Run the application: After completing the setup, you can start the SafeSpace application locally by running:

bash
Copy code
streamlit run app.py
This will launch the application in your default web browser.

Testing the Application
Once the app is running, follow these steps to test the functionality:

Input a message:

In the text input field, type a message to classify. You can try different messages, both positive and potentially offensive.
Select a sample message:

Alternatively, select one of the predefined sample messages from the dropdown menu provided in the app. Some example messages include:
"You are so inspiring. Keep up the great work!"
"Everyone thinks you're terrible. Just leave already."
"Thank you for your help on the project."
"You don't deserve to be here."
Click the "Detect" button:

Once you've entered or selected a message, click the Detect button to initiate the classification process. The app will analyze the message and display whether it is classified as Harassment or Safe, along with a confidence score.
Check Firebase:

After testing, the results (message, classification, and confidence) are saved to Firebase under the reports collection. You can verify this by checking the Firebase console.
Harassment Detection:

If the message is flagged as Harassment, the app will display safety tips, such as blocking or reporting the user, to assist the person in handling online harassment.
Error Handling:

If you encounter any issues such as missing dependencies or incorrect environment variable configurations, refer to the error messages in the terminal or the logs for debugging information.
Expected Results
Harassment Message: If the input message contains harmful or offensive content, it should be classified as "Harassment" with a corresponding confidence score (e.g., 0.75).
Safe Message: If the message is neutral or positive, it should be classified as "Safe" with a high confidence score (e.g., 0.95).
Troubleshooting
If you encounter any issues, try the following:

Ensure that Firebase credentials are set correctly in the .env file.
Ensure that all dependencies are installed properly by running pip install -r requirements.txt (if available).
Verify that the FireStore database is set up properly and that the app has the necessary access rights.
Running Unit Tests (Optional)
If you want to run any unit tests you have written for the application, use the following command:

bash
Copy code
python -m unittest discover tests/
This will automatically discover and run all tests located in the tests/ directory.

