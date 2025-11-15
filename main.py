"""
Cloud Database Manager App with User Authentication
Author: William Dario Delgado Florez
Course: BYU–Idaho – CSE 310 Cloud Databases Module (Sprint 3)
"""

import firebase_admin
from firebase_admin import credentials, firestore
import os
import requests

# ----------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------

API_KEY = "AIzaSyCQ6EhgFJqGzqcmGUeIHtJ0fFs_Tt6-elc"   # <- CHANGE THIS
SERVICE_ACCOUNT_FILE = "serviceAccount.json"     # <- Put your JSON file here


# ----------------------------------------------------------
# FIREBASE INITIALIZATION
# ----------------------------------------------------------

def initialize_firestore():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print("\n❌ Error: serviceAccount.json file not found.")
        print("Download it from Firebase > Project Settings > Service Accounts.\n")
        exit()

    cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
    firebase_admin.initialize_app(cred)
    print("✅ Firestore connection established.\n")
    return firestore.client()


# ----------------------------------------------------------
# AUTHENTICATION FUNCTIONS
# ----------------------------------------------------------

def signup():
    print("\n--- SIGN UP ---")
    email = input("Enter email: ")
    password = input("Enter password: ")

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}

    r = requests.post(url, json=payload)
    data = r.json()

    if "error" in data:
        print("❌ Sign-up failed:", data["error"]["message"], "\n")
    else:
        print("✅ Account created successfully!")
        print("UID:", data["localId"])
        print("ID Token:", data["idToken"], "\n")


def login():
    print("\n--- LOGIN ---")
    email = input("Enter email: ")
    password = input("Enter password: ")

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}

    r = requests.post(url, json=payload)
    data = r.json()

    if "error" in data:
        print("❌ Login failed:", data["error"]["message"], "\n")
        return None
    else:
        print("✅ Login successful!")
        print("Welcome,", email, "\n")
        return data["idToken"]  # returned token if needed


# ----------------------------------------------------------
# CRUD FUNCTIONS
# ----------------------------------------------------------

def add_data(db):
    print("\n--- ADD USER ---")
    name = input("Enter name: ")
    email = input("Enter email: ")
    data = {"name": name, "email": email}

    db.collection("users").add(data)
    print("✅ User added!\n")


def read_data(db):
    print("\n--- ALL USERS ---")
    docs = db.collection("users").stream()
    empty = True

    for doc in docs:
        empty = False
        print(f"🆔 {doc.id} | {doc.to_dict()}")

    if empty:
        print("No users found.")
    print("")


def update_data(db):
    print("\n--- UPDATE USER ---")
    doc_id = input("Document ID: ")
    field = input("Field to update (name/email): ")
    value = input("New value: ")

    doc_ref = db.collection("users").document(doc_id)
    if doc_ref.get().exists:
        doc_ref.update({field: value})
        print("✅ User updated!\n")
    else:
        print("❌ Document not found.\n")


def delete_data(db):
    print("\n--- DELETE USER ---")
    doc_id = input("Document ID: ")
    doc_ref = db.collection("users").document(doc_id)

    if doc_ref.get().exists:
        doc_ref.delete()
        print("🗑️ User deleted!\n")
    else:
        print("❌ Document not found.\n")


# ----------------------------------------------------------
# MENU SYSTEM
# ----------------------------------------------------------

def main_menu():
    print("""
===============================
 CLOUD DATABASE MANAGER APP 
===============================
1. Sign up (create account)
2. Log in
3. Add new data
4. View all data
5. Update data
6. Delete data
7. Exit
""")


def main():
    db = initialize_firestore()
    logged_in = False

    while True:
        main_menu()
        choice = input("Select an option: ")

        if choice == "1":
            signup()

        elif choice == "2":
            token = login()
            if token:
                logged_in = True

        elif choice in ["3", "4", "5", "6"] and not logged_in:
            print("❌ You must log in before performing CRUD operations.\n")

        elif choice == "3":
            add_data(db)

        elif choice == "4":
            read_data(db)

        elif choice == "5":
            update_data(db)

        elif choice == "6":
            delete_data(db)

        elif choice == "7":
            print("\n👋 Exiting program. Goodbye!\n")
            break

        else:
            print("❌ Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
