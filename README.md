SafeSpace is an AI tool developed to help women and girls recognize and respond to online harassment. By using the cardiffnlp/twitter-roberta-base-offensive model, the tool evaluates messages for potentially harmful content and classifies them as either "Harassment" or "Safe." Firebase integration enables user authentication and stores reports for further analysis, ensuring data security. The tool empowers women to stand up to online harassment, offering safety resources and providing support. By leveraging AI, SafeSpace works towards gender equality by making it easier for women and girls to safely engage with online spaces, thereby reducing the gender disparities present in digital interactions.

Testing Instructions for SafeSpace Application
To test the SafeSpace application locally and ensure its functionality, follow these steps:

Prerequisites
Before testing the application, ensure that you have the following tools installed on your machine:

Python 3.x
Streamlit library
Transformers library (by Hugging Face)
Firebase (for storage and reporting)
torch library
dotenv library (for environment variable management)
Google Cloud Firestore (for report storage)
You can install the required libraries using pip:

bash
Copy code
pip install streamlit transformers torch firebase-admin google-cloud-firestore python-dotenv
Setting Up the Environment
Clone the repository: First, clone the SafeSpace repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/safespace.git
cd safespace
Set up Firebase:

Create a Firebase project in the Firebase Console.

Download the Firebase Admin SDK credentials file and save it as firebase-adminsdk.json in your project folder.

Add the Firebase credentials to your environment variables by creating a .env file and setting the path:

bash
Copy code
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/firebase-adminsdk.json
Run the application: After setting up the environment and installing the necessary dependencies, you can run the SafeSpace app locally by executing the following command in your terminal:

bash
Copy code
streamlit run app.py
This will launch the Streamlit app in your default web browser.

Testing the Application
Once the app is running, you can test its core functionalities:

Input a message:

Use the text input field on the home screen to enter a message you want to classify. This message can be any form of text, whether it is positive, neutral, or potentially offensive.
Select a sample message:

You can also use the dropdown menu in the sample message section to choose from predefined sample messages. These include:
"You are so inspiring. Keep up the great work!"
"Everyone thinks you're terrible. Just leave already."
"Thank you for your help on the project."
"You don't deserve to be here."
Click the "Detect" button:

Once you’ve entered your text, click the Detect button to start the classification process. The application will analyze the message and display whether it has been flagged as "Harassment" or "Safe" along with a confidence level.
Check the report functionality:

After testing, the application will save the results (message, classification, and confidence) to Firebase under the reports collection. Check your Firebase console to see if the reports have been saved correctly.
Safety tips for Harassment:

If the message is classified as "Harassment," the app will display safety tips, such as blocking or reporting the user, and the “Harassment Detected” warning. These safety tips are provided to help users understand how to respond to online abuse.
Error handling:

If you encounter any issues, such as missing dependencies or environment variable misconfigurations, ensure that all the prerequisites are correctly set up. Check the error logs in the terminal for detailed messages.
Expected Results
Harassment Message: If the input message contains offensive or harmful content, the model should classify it as "Harassment" with a corresponding confidence level (e.g., 0.75).
Safe Message: If the message is neutral or positive, it should be classified as "Safe" with a high confidence score (e.g., 0.95).
Troubleshooting
If you face issues with Firebase integration, ensure your Firebase credentials are correctly set in the .env file, and verify that your Firebase project settings are configured to allow Firestore access.
If you encounter issues with Model loading or Torch, verify that the dependencies are correctly installed and compatible with your system.
