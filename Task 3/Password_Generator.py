# Password Generator: A Python GUI application to generate random, strong passwords with custom lengths and copy to clipboard.
# Built with tkinter, it uses a combination of characters from letters, digits, and punctuation.


import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to generate a password


def generate_password():
    try:
        length = int(password_length.get())
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        password = ''.join(random.choice(
            string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        password_result.set(password)
    except ValueError:
        messagebox.showerror(
            "Error", "Invalid input. Please enter a positive integer for the length.")


# Function to regenerate a new password with the same length


def regenerate_password():
    generate_password()

# Function to copy the generated password to the clipboard


def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_result.get())
    window.update()


# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Add space at the top
tk.Label(window, text="", font=("Arial", 14)).pack()

# Password Length Input
tk.Label(window, text="Enter Password Length:", font=("Arial", 14)).pack()
password_length = tk.Entry(window, font=("Arial", 14))
password_length.pack()

# Generate Password Button
tk.Button(window, text="Generate Password",
          command=generate_password, font=("Arial", 14)).pack()

# Display the generated password
password_result = tk.StringVar()
password_result_label = tk.Label(
    window, textvariable=password_result, font=("Arial", 16))
password_result_label.pack()

# Add space between buttons
tk.Label(window, text="", font=("Arial", 14)).pack()

# Regenerate Password Button
tk.Button(window, text="Regenerate Password",
          command=regenerate_password, font=("Arial", 14)).pack()

# Copy Password Button
tk.Button(window, text="Copy Password",
          command=copy_password, font=("Arial", 14)).pack()

# Start the GUI main loop
window.mainloop()
