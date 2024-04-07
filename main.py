import requests
import os
from time import sleep

link = "http://127.0.0.1:5050/users"

def register(email, username, password):
    data = {
        "email": email,
        "username": username,
        "password": password
    }

    response = requests.post(link, json=data)

    if response.status_code == 201:
        print("✔ User registered successfully!")
        main()
    else:
        print("Error - Unable to register user.")

def login(username, password):
    data = {
        "username": username,
        "password": password
    }

    response = requests.get(link, json=data)

    if response.status_code == 200:
        print("✔ Login successful!")
    elif response.status_code == 401:
        print("Invalid password.")
    elif response.status_code == 404:
        print("Username not found.")
    else:
        print("Error occurred.")

def show_menu():
    os.system('cls')
    menu = """
        [AuthMe - Genaro Arce]
    
    [1] - Login (username, password)
    [2] - Register (email, username, password)
    [3] - Exit

    """
    print(menu)

def main():
    show_menu()
    option = int(input("Insert your option >> "))

    if option == 1:
        username = input("Insert your username >> ")
        password = input("Insert your password >> ")
        login(username, password)
    elif option == 2:
        email = input("Insert your email >> ")
        username = input("Insert your username >> ")
        password = input("Insert your password >> ")
        register(email, username, password)
    else:
        exit()

if __name__ == "__main__":
    main()
