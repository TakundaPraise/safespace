SafeSpace is an AI tool developed to help women and girls recognize and respond to online harassment. By using the cardiffnlp/twitter-roberta-base-offensive model, the tool evaluates messages for potentially harmful content and classifies them as either "Harassment" or "Safe." Firebase integration enables user authentication and stores reports for further analysis, ensuring data security. The tool empowers women to stand up to online harassment, offering safety resources and providing support. By leveraging AI, SafeSpace works towards gender equality by making it easier for women and girls to safely engage with online spaces, thereby reducing the gender disparities present in digital interactions.

Testing Instructions for SafeSpace Application


Installation
Clone the repository:

bash
git clone https://github.com/your-username/safespace.git
cd safespace
Install dependencies:

bash
pip install -r requirements.txt
Set up Firebase:

Create a Firebase project and download the Firebase Admin SDK credentials as firebase-adminsdk.json.
Add the Firebase credentials to your .env file:
bash
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/firebase-adminsdk.json
Running the Application
Start the app with Streamlit:

bash
streamlit run app.py
Usage
Enter a message in the text input field or select a sample message.
Click "Detect" to check if the message contains harassment.
Results will show whether the message is "Harassment" or "Safe," along with the confidence level.
If harassment is detected, safety tips will be provided.
Firebase Integration
The app saves each report to Firebase under the reports collection for analysis.
Troubleshooting
Ensure Firebase credentials are set correctly in the .env file.
Run pip install -r requirements.txt if dependencies are missing.

