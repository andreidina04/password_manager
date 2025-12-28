import hashlib
import os

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

PIN_FILE = "pin.txt"

def setup_pin():
    pin = input("Create a PIN: ")
    with open(PIN_FILE, "w") as f:
        f.write(hash_pin(pin))
    print("PIN created!")
