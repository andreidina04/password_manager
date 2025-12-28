from cryptography.fernet import Fernet

# Generate key for the first time
key = Fernet.generate_key()
with open("key.key", "wb") as f:
    f.write(key)

print("Key generated")
