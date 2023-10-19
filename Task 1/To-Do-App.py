import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create the user interface elements
task_label = tk.Label(app, text="Enter a new task:")
task_label.pack()

task_input = tk.Entry(app)
task_input.pack()

task_listbox = tk.Listbox(app)
task_listbox.pack()


# Function to add a task to the list
def add_task():
    new_task = task_input.get()
    if new_task:
        task_listbox.insert(tk.END, new_task)
        task_input.delete(0, tk.END)
        save_tasks()

# Function to mark a task as done
def remove_task():
    selected_indices = task_listbox.curselection()
    if selected_indices:
        for index in selected_indices:
            task_listbox.delete(index)
        save_tasks()
    else:
        messagebox.showerror("Error", "Select a task to mark as done")

# Function to save tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a text file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Call the load_tasks function to populate the list when the application starts
load_tasks()

# Function to save tasks and quit the application
def save_and_quit():
    save_tasks()
    app.quit()

add_button = tk.Button(app, text="Add Task", command= add_task)
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
quit_button = tk.Button(app, text="Quit", command=save_and_quit)

add_button.pack()
remove_button.pack()
quit_button.pack()    

# Run the Application
app.mainloop()
