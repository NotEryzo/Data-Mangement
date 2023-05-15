# Data Management Project

import json

# Load Json file and create empty dictionary. Runs the function even if there is an error. 
try: 
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

# Sign up function and save the username and password to json file for login
def signup():
    while True:
        username = input("Enter your desired username: ")
        if username in users:
            print("Username already taken.")
        else: 
            password = input("Enter your password: ")
            users[username] = {"password": password}
            with open("users.json", "w") as f:
                json.dump(users, f)
            print("Signup successful!")
            break


# Ask the user for their username and password
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

    # Check if the username and password exist
        user = users.get(username)
        if user and user["password"] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

# Signup or login menu
while True:
    print("1. Signup")
    print("2. Login")
    choice = input("Enter a selection (1-2): ")

    if choice == 1:
        signup()
    elif choice == 2:
        login()
    else: 
        print("Please enter either 1 or 2")








    






















