# Rock-Paper-Scissors Game implemented as a GUI application using tkinter.
# The user can play against the computer and see the final score when the game ends.


import tkinter as tk
import random

# Initialize variables to keep track of user and computer scores, and the game state
user_score = 0
computer_score = 0
game_in_progress = False

# Function to determine the result of a round


def determine_winner(user_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    # Generate a random computer choice
    computer_choice = random.choice(choices)
    result = ""

    # Determine the winner or if it's a tie
    if user_choice == computer_choice:
        result = "It's a tie!"
        result_color = "orange"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result = "You win!"
        result_color = "green"
    else:
        computer_score += 1
        result = "Computer wins!"
        result_color = "red"

    # Display the result of the round
    display_result(user_choice, computer_choice, result, result_color)

# Function to display the result of the round


def display_result(user_choice, computer_choice, result, result_color):
    result_label.config(text=result, font=("Arial", 18), fg=result_color)
    result_label2.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}", font=("Arial", 14))

# Function to start a new round


def play_round(user_choice):
    determine_winner(user_choice)

# Function to start a new game


def start_game():
    global game_in_progress
    game_in_progress = True
    result_label.config(text="")
    clear_display()  # Clear the display
    start_button.config(state=tk.DISABLED)
    quit_button.config(state=tk.NORMAL)
    enable_choice_buttons()

# Function to end the game and display the final score


def end_game():
    global game_in_progress
    game_in_progress = False
    display_final_score()
    start_button.config(state=tk.NORMAL)
    quit_button.config(state=tk.DISABLED)
    disable_choice_buttons()

# Function to enable choice buttons


def enable_choice_buttons():
    for button in choice_buttons:
        button.config(state=tk.NORMAL)

# Function to disable choice buttons


def disable_choice_buttons():
    for button in choice_buttons:
        button.config(state=tk.DISABLED)

# Function to display the final score


def display_final_score():
    result_label.config(text="Final Score\nYou: " +
                        str(user_score) + "\nComputer: " + str(computer_score))
    # Clear the user and computer choices
    result_label2.config(text="")

# Function to clear the display


def clear_display():
    result_label.config(text="")
    result_label2.config(text="")


# Create the main window for the game
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")

# Create and configure a label for the title
title_label = tk.Label(
    window, text="Rock-Paper-Scissors Game", font=("Arial", 20))
title_label.pack(pady=10)


# Create and configure labels to display game results
result_label = tk.Label(window, text="", font=("Arial", 18))
result_label2 = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)
result_label2.pack(pady=5)

# Create and configure buttons for game choices
button_font = ("Arial", 14)
choices = ["Rock", "Paper", "Scissors"]

# Create a list to store the choice buttons (Rock, Paper, Scissors)
choice_buttons = []

# Create a frame to hold the choice buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create choice buttons for Rock, Paper, and Scissors
for choice in choices:
    # Create a button for each choice with a specified text and font
    # When a button is clicked, it calls the play_round function with the respective choice
    button = tk.Button(button_frame, text=choice,
                       command=lambda c=choice: play_round(c), font=button_font, state=tk.DISABLED)
    # Add the button to the list of choice_buttons
    choice_buttons.append(button)
    # Place the button in the frame and add padding
    button.pack(side=tk.LEFT, padx=10)

# Create buttons for starting and quitting the game
start_button = tk.Button(window, text="Start Game",
                         command=start_game, font=("Arial", 16))
quit_button = tk.Button(window, text="Quit Game",
                        command=lambda: [end_game(), display_final_score()], state=tk.DISABLED, font=("Arial", 16))

# Pack the start and quit buttons
start_button.pack(pady=10)
quit_button.pack(pady=10)

# Start the GUI application
window.mainloop()
