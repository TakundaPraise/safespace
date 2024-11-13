SafeSpace is an AI tool developed to help women and girls recognize and respond to online harassment. By using the cardiffnlp/twitter-roberta-base-offensive model, the tool evaluates messages for potentially harmful content and classifies them as either "Harassment" or "Safe." Firebase integration enables user authentication and stores reports for further analysis, ensuring data security. The tool empowers women to stand up to online harassment, offering safety resources and providing support. By leveraging AI, SafeSpace works towards gender equality by making it easier for women and girls to safely engage with online spaces, thereby reducing the gender disparities present in digital interactions.

Testing Instructions for SafeSpace Application

# SafeSpace - Online Harassment Detector for Women and Girls

## Overview
SafeSpace is an AI-powered tool designed to help women and girls identify online harassment. It uses the **cardiffnlp/twitter-roberta-base-offensive** model to classify messages as either **Harassment** or **Safe**. The tool integrates with **Firebase** to securely store reports and provide users with safety tips.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/safespace.git
    cd safespace
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Firebase**:
    - Create a Firebase project and download the Firebase Admin SDK credentials as `firebase-adminsdk.json`.
    - Add the Firebase credentials to your `.env` file:
    
    ```bash
    GOOGLE_APPLICATION_CREDENTIALS=path/to/your/firebase-adminsdk.json
    ```

## Running the Application

Start the app with Streamlit:

```bash
streamlit run app.py

