import hashlib
import os

# Function to hash a PIN using SHA-256
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

PIN_FILE = "pin.txt"  # File where the hashed PIN will be stored

# Function to set up a new PIN
def setup_pin():
    pin = input("Create a PIN: ")
    with open(PIN_FILE, "w") as f:
        f.write(hash_pin(pin))
    print("PIN created!")
