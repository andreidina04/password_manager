import customtkinter
import customtkinter as ctk
from cryptography.fernet import Fernet
from pin import setup_pin, hash_pin, PIN_FILE
import os

app = ctk.CTk()
app.geometry("500x500")
app.title("Password Manager")
FILE_NAME = "my_passwords.txt"

# Load encryption key used for password encryption/decryption
def load_key():
    with open("key.key", "rb") as f:
        return f.read()

key = load_key()
fer = Fernet(key)

# Create PIN on first run (if no PIN file exists)

if not os.path.exists(PIN_FILE):
    setup_pin()

pin_frame = ctk.CTkFrame(app, fg_color="#141936")
menu_frame = ctk.CTkFrame(app, fg_color="#141936")
add_frame = ctk.CTkFrame(app, fg_color="#141936")
view_frame = ctk.CTkFrame(app, fg_color="#141936")

# Show only one frame at a time
def show_frame(frame):
    for f in (pin_frame, menu_frame, add_frame, view_frame):
        f.pack_forget()
    frame.pack(expand=True, fill="both")

ctk.CTkLabel(pin_frame, text="Password Manager", font=("Arial", 20, "bold")).pack(pady=20)
pin_entry = ctk.CTkEntry(pin_frame, placeholder_text="Enter PIN", show="*", text_color="white", width=300, height=50, corner_radius= 20, justify="center", fg_color="#212946",border_width=1, border_color="#FFFFFF")
pin_entry.pack(pady=20)

pin_result = ctk.CTkLabel(pin_frame, text="")
pin_result.pack()

# Verify entered PIN against stored hash
attempts = 4
def verify_pin(event=None):
    global attempts
    with open(PIN_FILE) as f:
        saved = f.read()
    if hash_pin(pin_entry.get()) == saved: # Checking if the entered pin is the same as the saved one
        show_frame(menu_frame)
    else:
            attempts -= 1
            if attempts > 0:
                pin_result.configure(text=f"Wrong PIN. Attempts left: {attempts}", text_color="red", font=("Arial", 14, "bold"))
            else:
                pin_result.configure(text=f"{attempts} attempts left! Closing the app...",text_color="red", font=("Arial", 14, "bold"))
                app.after(800, exit)

ctk.CTkButton(pin_frame,text="Verify", command=verify_pin, fg_color="#FFFFFF", text_color="#141936", corner_radius=50, hover_color="#ADADAD", width=200, height=40, font=("Arial", 15, "bold")).pack(pady=10)
ctk.CTkLabel(menu_frame, text="Password Manager", font=("Arial", 20, "bold")).pack(pady=20)
ctk.CTkButton(menu_frame, text="Add Password", command=lambda: show_frame(add_frame), fg_color="#FFFFFF", text_color="#141936", corner_radius=50, hover_color="#ADADAD", width=200, height=40, font=("Arial", 15, "bold")).pack(pady=10)
ctk.CTkButton(menu_frame, text="View Passwords", command=lambda: show_frame(view_frame), fg_color="#FFFFFF", text_color="#141936", corner_radius=50, hover_color="#ADADAD", width=200, height=40, font=("Arial", 15, "bold")).pack(pady=10)

app_entry = ctk.CTkEntry(add_frame, placeholder_text="Application", text_color="white", width=300, height=50, corner_radius= 20, fg_color="#212946",border_width=1, border_color="#FFFFFF")
user_entry = ctk.CTkEntry(add_frame, placeholder_text="Username", text_color="white", width=300, height=50, corner_radius= 20, fg_color="#212946",border_width=1, border_color="#FFFFFF")
pwd_entry = ctk.CTkEntry(add_frame, placeholder_text="Password", text_color="white", width=300, height=50, corner_radius= 20, fg_color="#212946",border_width=1, border_color="#FFFFFF")

app_entry.pack(pady=5)
user_entry.pack(pady=5)
pwd_entry.pack(pady=5)

add_msg = ctk.CTkLabel(add_frame, text="")
add_msg.pack(pady=5)

# Encrypt and save password to file
def save_password():
    app_name = app_entry.get()
    user = user_entry.get()
    pwd = pwd_entry.get()

    if not app_name or not user or not pwd:
        add_msg.configure(text="All fields required", text_color="red", font=("Arial", 12, "bold"))
        return

    encrypted = fer.encrypt(pwd.encode()).decode() # Crypt saved passwords
    with open(FILE_NAME, "a") as f:
        f.write(f"{app_name}|{user}|{encrypted}\n")

    add_msg.configure(text="Password saved!", text_color="green", font=("Arial", 12, "bold"))
    app_entry.delete(0, "end")
    user_entry.delete(0, "end")
    pwd_entry.delete(0, "end")

ctk.CTkButton(add_frame, text="Save", command=save_password, fg_color="#FFFFFF", text_color="#141936", corner_radius=50, hover_color="#ADADAD", width=200, height=40, font=("Arial", 15, "bold")).pack(pady=10)
ctk.CTkButton(add_frame, text="Back", command=lambda: show_frame(menu_frame), fg_color="#303030", text_color="white", corner_radius=50, hover_color="#4D4D4D", width=200, height=40, font=("Arial", 15, "bold")).pack()

textbox = ctk.CTkTextbox(view_frame, width=400, height=250, fg_color="#212946", text_color="white", border_width=1, border_color="#212852")
textbox.pack(pady=20)

# Load and decrypt stored passwords
def load_passwords():
    textbox.configure(state="normal", fg_color="#212946", text_color="white", border_width=1, border_color="#212852")
    textbox.delete("1.0", "end")

    if not os.path.exists(FILE_NAME):
        textbox.insert("end", "No passwords stored.")
    else:
        try:
            with open(FILE_NAME) as f:
                has_passwords = False
                for line in f:
                    has_passwords = True
                    app_name, user, enc = line.strip().split("|")
                    pwd = fer.decrypt(enc.encode()).decode() # Decrypt stored passwords
                    textbox.insert("end", f"Application: {app_name}\nUser: {user}\nPassword: {pwd}\n\n")
                if not has_passwords:
                    textbox.insert("end", "Hmmm...no passwords stored.")
        except Exception as e:
            textbox.insert("end", f"An error occurred: {e}")
    textbox.configure(state="disabled")

ctk.CTkButton(view_frame, text="Refresh Passwords", command=load_passwords, fg_color="#FFFFFF", text_color="#141936", corner_radius=50, hover_color="#ADADAD", width=200, height=40, font=("Arial", 15, "bold")).pack()
ctk.CTkButton(view_frame, text="Back", command=lambda: show_frame(menu_frame), fg_color="#303030", text_color="white", corner_radius=50, hover_color="#4D4D4D", width=200, height=40, font=("Arial", 15, "bold")).pack(pady=10)
pin_entry.bind("<Return>", verify_pin) # Enter bind for Verify button
show_frame(pin_frame)
app.mainloop()
