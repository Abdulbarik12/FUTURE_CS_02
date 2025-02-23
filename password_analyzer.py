import tkinter as tk
import re
import hashlib
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    
    # Criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password)
    uppercase_criteria = re.search(r"[A-Z]", password)
    number_criteria = re.search(r"[0-9]", password)
    special_criteria = re.search(r"[@$!%*?&]", password)
    
    # Common Weak Passwords
    common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]
    if password in common_passwords:
        return "Very Weak", "Commonly used password! Change it!"
    
    # Calculate Strength Score
    if length_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_criteria:
        strength += 1
    
    # Assign Remarks
    if strength == 1 or strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 5:
        remarks = "Very Strong"
    
    return remarks, "Strength Score: {}/5".format(strength)

def analyze_password():
    password = entry_password.get()
    strength, message = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}\n{message}", fg="blue")

def encrypt_password():
    password = entry_password.get()
    if password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        messagebox.showinfo("Encrypted Password", f"SHA-256 Hash:\n{hashed_password}")
    else:
        messagebox.showwarning("Input Error", "Please enter a password")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x300")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial", 12))
entry_password.pack(pady=5)

btn_analyze = tk.Button(root, text="Analyze Strength", command=analyze_password, font=("Arial", 12))
btn_analyze.pack(pady=5)

btn_encrypt = tk.Button(root, text="Encrypt Password", command=encrypt_password, font=("Arial", 12))
btn_encrypt.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()
