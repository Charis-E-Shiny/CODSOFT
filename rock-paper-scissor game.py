import random

def get_user_choice():
    print("Choose one:")
    print("1. Rock \U0001FAA8")
    print("2. Paper \U0001F4C3")
    print("3. Scissors \u2702\ufe0f")
    choice = input("Enter the number of your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        choice = input("Enter the number of your choice (1-3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    outcomes = {
        (1, 3): "win",
        (2, 1): "win",
        (3, 2): "win",
        (3, 1): "lose",
        (1, 2): "lose",
        (2, 3): "lose",
    }
    if user_choice == computer_choice:
        return "tie"
    return outcomes.get((user_choice, computer_choice), "error")
options = {1: "Rock \U0001FAA8", 2: "Paper \U0001F4C3", 3: "Scissors \u2702\ufe0f"}
print("Welcome to Rock, Paper, Scissors! \U0001F973")
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {options[user_choice]} \U0001F44D")
    print(f"Computer chose: {options[computer_choice]} \U0001F916")

    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie! \U0001F610")
    elif result == "win":
        print("You win! \U0001F60E")
    elif result == "lose":
        print("You lose! \U0001F622")
    else:
        print("Unexpected error occurred. \U0001F914")
    play_again = input("Do you want to play again? (yes/no): \U0001F4AC ").lower()

    if play_again != "yes":
        print("Thanks for playing! Goodbye! \U0001F44B")
        break


