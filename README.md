# Cloud Database Manager App (Firestore + Python)

This project is a **Python application** that connects to a **Google Firestore Cloud Database** using the **Firebase Admin SDK**.  
It supports full **CRUD operations** (Create, Read, Update, Delete) and includes **Firebase Authentication** (email + password login), which completes the stretch challenge requirement for this Sprint.

## Features

### Required Features
- Create a cloud database (Firestore)
- Query data from a collection
- Add new documents
- Update existing documents
- Delete documents

### Stretch Challenge (Completed)
- **User Authentication** (Firebase Auth REST API)

## How to Run the Program

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Setup Firebase
1. Go to Firebase Console → Create a Project  
2. Enable:
   - **Firestore Database**
   - **Firebase Authentication**
3. Go to **Project Settings → Service Accounts**  
4. Click **Generate New Private Key**  
5. Save it as:
   serviceAccount.json
(*Do NOT upload this to GitHub.*)

6. Get your Web API Key  
   Firebase Console → Project Settings → General → Web API Key

Paste it inside `main.py:
``python
API_KEY = "YOUR_API_KEY"

RUN THE APP 
pyhton. main.py

Menu Options
Sign up (create Firebase Auth account)
Log in
Add new data to Firestore
View all users
Update user data
Delete user
Exit
All CRUD operations require successful login.

Development Environment
Python 3.10+
Firebase Admin SDK
Firestore Database
Firebase Auth (REST API)
macOS/Windows/Linux

Useful Links
https://firebase.google.com/docs/firestore
https://firebase.google.com/docs/auth
https://firebase.google.com/docs/admin/setup
https://www.guru99.com/nosql-tutorial.html
https://www.mongodb.com/resources/cloud-database

Future Work
 Add GUI using Tkinter or Flask
 Add Firestore real-time listener
 Add multi-collection relationships
 Deploy backend to Google Cloud Functions
 Add role-based access control
