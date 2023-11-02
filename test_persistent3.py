print('test_persistent___')
'''
To modify the script to ask the user how many times they want to play and to keep score, you'll need to add a few things:
Ask the user how many rounds they want to play.
Keep track of the scores in each round.
Display the final scores after all rounds are played.
'''
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

def no_of_times_user_wants_to_play():
    platy_times = int(input(" Enter no of times you want to play"))
    return platy_times

if __name__ == "__main__":
    playt_times = no_of_times_user_wants_to_play()
    results = []
    res = {}
    for i in range(playt_times):
        result = main()
        results.append(result)

    for val in set(results):
        res[val]=results.count(val)
    print(res)

    if res['You lose!']>res['You win!']:
        print('you Lost the match')
    elif res['You lose!']==res['You win!']:
        print('its a tie.')
    else:
        print('You Won the match..')