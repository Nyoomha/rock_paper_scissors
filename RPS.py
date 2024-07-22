import random
from tkinter import *

def get_player_choice():
    while True:
        choice = input("Enter your option: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Please try again\n")

def computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)


def det_winner(player_choice_result, computer_choice_result):
    if (player_choice_result == 'rock' and computer_choice_result == 'scissors') or \
        (player_choice_result == 'scissors' and computer_choice_result == 'paper') or \
        (player_choice_result == 'paper' and computer_choice_result == 'rock'):
        print (player_choice_result, "beats", computer_choice_result, "you win!" )
    elif player_choice_result == computer_choice_result:
        print("we both chose", player_choice_result, "its a tie!")
    else:
        print(computer_choice_result, "beats", player_choice_result, "I win!")


def main():
    print("\nHello! Welcome to Rock, Paper, and Scissors\n")
    computer_choice_result = computer_choice()
    player_choice_result = get_player_choice()
    det_winner(player_choice_result, computer_choice_result)

if __name__ == "__main__":
    main()