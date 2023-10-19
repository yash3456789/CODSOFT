# Simple calculator app using tkinter for creating a GUI and performing basic arithmetic operations.

import tkinter as tk
from tkinter import ttk

# Function to perform the calculation


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)
        else:
            result.set("Invalid operation")
    except ValueError:
        result.set("Invalid input")

# Function to clear input and result


def clear():
    entry_num1.delete(0, 'end')
    entry_num2.delete(0, 'end')
    operation_menu.set('+')
    result.set("")

# Function to quit the application


def quit_app():
    window.destroy()


# Create the calculator window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x300")  # Set window dimensions

# Title label
title_label = tk.Label(window, text="Simple Calculator", font=("Arial", 18))
title_label.pack(pady=20)  # Pushed down by 20 pixels

# Input fields for numbers
entry_num1 = tk.Entry(window, font=("Arial", 14))
entry_num2 = tk.Entry(window, font=("Arial", 14))

# Dropdown for selecting the operation
operation_var = tk.StringVar()
operation_menu = ttk.Combobox(
    window, textvariable=operation_var, values=['+', '-', '*', '/'], font=("Arial", 16))
operation_menu.set('+')  # Set the default operation

# Button for calculating
calculate_button = ttk.Button(window, text="Calculate", command=calculate)

# Clear button
clear_button = ttk.Button(window, text="Clear", command=clear)

# Display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Arial", 16))

# Quit button
quit_button = ttk.Button(window, text="Quit", command=quit_app)

# Place widgets in the window
entry_num1.pack(pady=5)
entry_num2.pack(pady=5)
operation_menu.pack(pady=5)
calculate_button.pack(pady=10)
clear_button.pack(pady=5)
result_label.pack(pady=10)
quit_button.pack(pady=10)

# Start the calculator application
window.mainloop()
