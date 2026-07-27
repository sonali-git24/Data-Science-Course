import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

# Function to play game
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Decide winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update labels
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(
        text=f"Score  You: {user_score}   Computer: {computer_score}"
    )

# Reset Game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_label.config(text="You chose:")
    computer_label.config(text="Computer chose:")
    result_label.config(text="")
    score_label.config(text="Score  You: 0   Computer: 0")


# Create Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x350")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

rock_btn = tk.Button(
    button_frame,
    text="Rock",
    width=10,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(
    button_frame,
    text="Paper",
    width=10,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(
    button_frame,
    text="Scissors",
    width=10,
    command=lambda: play("Scissors")
)
scissor_btn.grid(row=0, column=2, padx=5)

# Labels
user_label = tk.Label(root, text="You chose:", font=("Arial", 12), bg="lightblue")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer chose:", font=("Arial", 12), bg="lightblue")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="lightblue")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score  You: 0   Computer: 0", font=("Arial", 12), bg="lightblue")
score_label.pack(pady=5)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

# Run Window
root.mainloop()