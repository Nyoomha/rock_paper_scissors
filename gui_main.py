import random
from tkinter import *
from tkinter import messagebox 
import tkinter as ttk

app = ttk.Tk()

canvas_widget = Canvas(app, width=250, height=250)
canvas_widget.grid(row=0, column=0, padx=10, pady=10)
  
label_widget1 = Label(app, text="Enter rock, paper, or scissors")
label_widget1.grid(row=1, column=0, pady=10)

entry_widget1 = Entry(app, width=20)
entry_widget1.grid(row=2, column=0, pady=10)

def get_player_choice():
    user_choice = entry_widget1.get().strip().lower() 

    if user_choice in ['rock', 'paper', 'scissors']:
        return user_choice
    else:
        messagebox.showinfo("Please try again") 

def computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def det_winner():
    player_choice_result = get_player_choice()

    if player_choice_result:
        computer_choice_result = computer_choice()
        
        if (player_choice_result == 'rock' and computer_choice_result == 'scissors') or \
            (player_choice_result == 'scissors' and computer_choice_result == 'paper') or \
            (player_choice_result == 'paper' and computer_choice_result == 'rock'):
            messagebox.showinfo("Result", f"{player_choice_result} beats {computer_choice_result} you win!")
        elif player_choice_result == computer_choice_result:
            messagebox.showinfo("Result", f"we both chose {player_choice_result} its a tie!")
        else:
            messagebox.showinfo("Result", f"{computer_choice_result} beats {player_choice_result} I win!")

        entry_widget1.delete(0, END)

button_widget = Button(app, text='Submit', command=det_winner)
button_widget.grid(row=3, column=0, pady=10)

app.mainloop()