import random
from tkinter import *
from tkinter import messagebox 
import tkinter as ttk

# fix submit button and make code compare user input to computer choice

root = ttk.Tk()
root.geometry("600x400")

choice_var = ttk.StringVar()

def submit():
 
    player_choice_result = choice_var.get()
     
    print("Rock, Paper, or Scissors?: " + player_choice_result)
    if player_choice_result in ['rock', 'paper', 'scissors']:
        return player_choice_result
    else:
        print("Please try again\n")
     
    choice_var.set("")

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

computer_choice_result = computer_choice()
player_choice_result = submit()

def det_winner(player_choice_result, computer_choice_result):
    if (player_choice_result == 'rock' and computer_choice_result == 'scissors') or \
        (player_choice_result == 'scissors' and computer_choice_result == 'paper') or \
        (player_choice_result == 'paper' and computer_choice_result == 'rock'):
        print (player_choice_result, "beats", computer_choice_result, "you win!" )
    elif player_choice_result == computer_choice_result:
        print("we both chose", player_choice_result, "its a tie!")
    else:
        print(computer_choice_result, "beats", player_choice_result, "I win!")

def result():
    #det_winner(player_choice_result, computer_choice_result)
    messagebox.showinfo(det_winner(player_choice_result, computer_choice_result)) 
   

name_label = ttk.Label(root, text = 'Choice', font=('calibre',10, 'bold'))
name_entry = ttk.Entry(root,textvariable = choice_var, font=('calibre',10,'normal'))
sub_btn = ttk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
root.mainloop()