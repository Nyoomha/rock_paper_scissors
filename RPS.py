import random

options = ['rock', 'paper', 'scissors']

print("\nHello! Welcome to Rock, Paper, and Scissors\n")

choice = input("Enter your option: ").lower()
computer_choice = random.choice(options)

#rock_computer():

if choice not in ['rock', 'paper', 'scissors']:
    print("Please try again")
else:
    if choice == 'rock':
        if computer_choice == 'paper':
            print(computer_choice,"beats", choice, "I won!")
        elif computer_choice == 'scissors':
            print(choice,"beats", computer_choice, "you won!")
        else:
            print("We both selected", choice, "its a tie!")
        
    if choice == 'paper':
        if computer_choice == 'scissors':
            print(computer_choice,"beats", choice, "I won!")
        elif computer_choice == 'rock':
            print(choice,"beats", computer_choice, "you won!")
        else:
            print("We both selected", choice, "its a tie!")

    if choice == 'scissors':
        if computer_choice == 'rock':
            print(computer_choice,"beats", choice, "I won!")
        elif computer_choice == 'paper':
            print(choice,"beats", computer_choice, "you won!")
        else:
            print("We both selected", choice, "its a tie!")