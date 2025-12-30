import customtkinter
from cryptography.fernet import Fernet
from pin import setup_pin, hash_pin, PIN_FILE
import os
import customtkinter as ctk

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Password Manager")
pin_frame = ctk.CTkFrame(app)
pin_frame.pack(expand=True)
pin_entry = ctk.CTkEntry(app, placeholder_text="Enter PIN:", show="*")
pin_entry.pack(pady=10)
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)
app_entry = None
user_entry = None
pwd_entry = None
message_label = None
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

def show_main_menu():
    global main_frame
    main_frame = ctk.CTkFrame(app)
    main_frame.pack(expand=True)

    add_btn = ctk.CTkButton(main_frame, text="Add Password", command=show_add)
    view_btn = ctk.CTkButton(main_frame, text="View Passwords", command=view)

    add_btn.pack(pady = 20)
    view_btn.pack(pady = 20)


def show_add():
    global add_frame, app_entry, pwd_entry, user_entry, message_label
    main_frame.pack_forget()
    add_frame = ctk.CTkFrame(app)
    add_frame.pack(expand=True)
    app_entry = ctk.CTkEntry(add_frame, placeholder_text="Application Name:")
    user_entry = ctk.CTkEntry(add_frame, placeholder_text="Username")
    pwd_entry = ctk.CTkEntry(add_frame, placeholder_text="Password")

    app_entry.pack(pady=10)
    user_entry.pack(pady=10)
    pwd_entry.pack(pady=10)
    add_button = ctk.CTkButton(add_frame, text="Save", command=add)
    add_button.pack(pady=20)
    message_label = ctk.CTkLabel(add_frame, text="", text_color="green")
    message_label.pack(pady=10)
# Verify user PIN before sensitive actions
def verify_pin():
    pin = pin_entry.get()
    with open(PIN_FILE, "r") as f:
        saved_hash = f.read()
    if hash_pin(pin) == saved_hash:
        result_label.configure(text="PIN OK", text_color="green")
        pin_entry.pack_forget()
        result_label.pack_forget()
        validate_pin.pack_forget()
        show_main_menu()
    else:
        result_label.configure(text="Wrong PIN", text_color="red")
        return False

validate_pin = ctk.CTkButton(app, text="Verify PIN", command=verify_pin)
validate_pin.pack(pady=10)
# Add new password entry
def add():
    app_name = app_entry.get()
    user= user_entry.get()
    pwd = pwd_entry.get()

    # Prevent breaking file format
    if "|" in app_name or "|" in user:
        message_label.configure(text="Character '|' is not allowed!", text_color="red")
        return
    if len(user) == 0 or len(pwd) == 0 or len(app_name) == 0:
        message_label.configure(text="Empty space is not allowed!", text_color="red")
        return
    # Encrypt password before saving
    encrypted = fer.encrypt(pwd.encode()).decode()

    with open(FILE_NAME, "a") as f:
        f.write(f"{app_name}|{user}|{encrypted}\n")
    message_label.configure(text="Password saved!", text_color="green")

    app_entry.delete(0, "end")
    user_entry.delete(0, "end")
    pwd_entry.delete(0, "end")
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
    mode = input("(add/view/q): ").lower()
    if mode == "q":
        print("Application is closing...")
        exit()
    elif mode == "add":
        if verify_pin():  # only allow adding if PIN is correct
            add()
    elif mode == "view":
        if verify_pin():  # only allow viewing if PIN is correct
            view()
    else:
        print("Invalid mode")

app.mainloop()
