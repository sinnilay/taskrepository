import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "Computer wins!"

    if user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "Computer wins!"

    if user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "Computer wins!"

# Main game loop
while True:
    print("Rock, Paper, Scissors - Enter your choice: ")
    user_choice = input("rock, paper, scissors or quit: ").lower()

    if user_choice == "quit":
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
