# 🛡️ CLI Password Manager

A **secure and user-friendly command-line password manager** written in Python.  
Store, view, and manage your passwords locally with **Fernet encryption** and **PIN-based authentication**.

---

## ✨ Features

- 🔹 **Add new passwords** for applications/accounts  
- 🔹 **View stored passwords** (requires PIN)  
- 🔹 **PIN protection** using SHA-256 hashing  
- 🔹 **Passwords encrypted** with Fernet symmetric encryption  
- 🔹 **Input validation** to prevent errors and ensure security  

## ⚠️ Future Updates

🔹 Delete passwords
🔹 Change PIN
🔹 Search functionality
🔹 GUI interface (Tkinter or PySimpleGUI)
🔹 Limit incorrect PIN attempts

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+  
- `cryptography` library  

Install the dependency:

```bash```
```pip install cryptography```

## 🛠️ Setup

Generate a Fernet key (run once):
```python generate_key.py```
This creates key.key, used for encrypting/decrypting your passwords.

Run the main program:
```python main.py```

On first run, you'll be prompted to create a PIN.
This PIN will be required for viewing passwords.
Passwords are stored locally in my_passwords.txt.

## 🧠 What I Learned

During the development of this CLI Password Manager, I gained hands-on experience with:
Python file handling – reading, writing, and managing local files safely.
Data encryption – using Fernet to securely encrypt and decrypt sensitive information.
User authentication – implementing a PIN system with SHA-256 hashing to protect access.
Error handling and input validation – ensuring the program handles edge cases like empty files, invalid inputs, or forbidden characters.
Modular code structure – separating functionality into modules (main.py, pin.py, generate_key.py) for better readability and maintainability.
CLI application design – creating a user-friendly command-line interface with menus and prompts.
Security best practices – understanding the difference between encryption keys and authentication, and protecting sensitive files from being exposed.

## 📝 Usage
<img width="462" height="339" alt="image" src="https://github.com/user-attachments/assets/9ad356ab-b156-4ace-bb13-fe991180d100" />
<img width="1056" height="117" alt="image" src="https://github.com/user-attachments/assets/eebc1701-e82a-4706-9015-ab09e94b1dcb" />

