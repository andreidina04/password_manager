from cryptography.fernet import Fernet
from pin import setup_pin, hash_pin, PIN_FILE
import os

FILE_NAME = "my_passwords.txt"

# Load encryption key from file
def load_key():
    with open("key.key", "rb") as f:
        return f.read()

key = load_key()
fer = Fernet(key)

# Setup PIN on first run
if not os.path.exists(PIN_FILE):
    setup_pin()

# Verify user PIN before sensitive actions
def verify_pin():
    pin = input("Enter PIN: ")
    with open(PIN_FILE, "r") as f:
        saved_hash = f.read()
    if hash_pin(pin) == saved_hash:
        return True
    else:
        print("Wrong PIN! Try again.")
        return False

# Add new password entry
def add():
    app = input("Application Name: ")
    user = input("Account Name: ")
    pwd = input("Account Password: ")

    # Prevent breaking file format
    if "|" in app or "|" in user:
        print("Character '|' is not allowed!")
        return

    # Encrypt password before saving
    encrypted = fer.encrypt(pwd.encode()).decode()

    with open(FILE_NAME, "a") as f:
        f.write(f"{app}|{user}|{encrypted}\n")

# View stored passwords
def view():
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:  # skip empty lines
                    continue
                app, user, enc_pwd = line.split("|")
                decrypted = fer.decrypt(enc_pwd.encode()).decode()
                print(f"App: {app} | User: {user} | Password: {decrypted}")
    except FileNotFoundError:
        print("File not found.")

# Main program loop
while True:
    mode = input("(add/view/q): ").lower()
    if mode == "q":
        print("Application is closing...")
        break
    elif mode == "add":
        if verify_pin():  # only allow adding if PIN is correct
            add()
    elif mode == "view":
        if verify_pin():  # only allow viewing if PIN is correct
            view()
    else:
        print("Invalid mode")
