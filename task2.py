import tkinter as tk
from tkinter import messagebox
import random as r

comp_num = r.randint(0, 100)

def check_guess():
    try:
        user_guess = int(entry.get())

        if user_guess == comp_num:
            messagebox.showinfo("Congratulations", f"Your Guess is Correct!\nThe Number was {comp_num}")
            root.destroy()
        elif user_guess > comp_num:
            result_label.config(text="Guess a little lower!")
        else:
            result_label.config(text="Guess a little higher!")
        entry.delete(0, tk.END)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x200") 


label = tk.Label(root, text="Enter Your Guess:")
label.pack(padx=5, pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", command=check_guess)
guess_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
