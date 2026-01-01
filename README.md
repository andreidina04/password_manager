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
- 🔹 **Limit incorrect PIN attempts** to prevent spamming pins
- 🔹 **GUI interface (Custom Tkinter)**
## ⚠️ Future Updates

🔹 Delete passwords
🔹 Change PIN
🔹 Search functionality
🔹 GUI interface (Tkinter or CTkinter) ✅
🔹 Limit incorrect PIN attempts ✅

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

📂 Python file handling – reading, writing, and managing local files safely
🔐 Data encryption – using Fernet to securely encrypt and decrypt sensitive information
🛡️ User authentication – implementing a PIN system with SHA-256 hashing
⚠️ Error handling and input validation – handling empty files, invalid inputs, and forbidden characters
🧩 Modular code structure – separating functionality into modules (main.py, pin.py, generate_key.py)
💻 CLI application design – creating a user-friendly command-line interface with menus and prompts
🔒 Security best practices – understanding the difference between encryption keys and authentication, and protecting sensitive files

## 📝 Usage - Before
<img width="462" height="339" alt="image" src="https://github.com/user-attachments/assets/9ad356ab-b156-4ace-bb13-fe991180d100" />
<img width="1056" height="117" alt="image" src="https://github.com/user-attachments/assets/eebc1701-e82a-4706-9015-ab09e94b1dcb" />

## 📝 Usage - After (Still in work)

<img width="533" height="555" alt="image" src="https://github.com/user-attachments/assets/406660b9-57fc-4a57-ac07-9a8a4756f308" />
<img width="502" height="530" alt="image" src="https://github.com/user-attachments/assets/4eb1b5b8-943d-4736-abc2-15579d912be4" />
<img width="496" height="527" alt="image" src="https://github.com/user-attachments/assets/2e090d97-51ad-4346-88ca-feeced346a6f" /> - Updated with attempts (default by 4)
<img width="494" height="525" alt="image" src="https://github.com/user-attachments/assets/7999fd44-2800-4288-a43b-81c24248d274" />
<img width="499" height="529" alt="image" src="https://github.com/user-attachments/assets/a9272035-7468-4b51-85e8-e48397f45a5c" />
