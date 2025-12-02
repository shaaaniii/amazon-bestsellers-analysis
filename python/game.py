import tkinter as tk
import random

choices = {"s": "🐍 Snake", "w": "💧 Water", "g": "🔫 Gun"}

def play(user_choice):
    computer_choice = random.choice(list(choices.keys()))
    result = ""

    if user_choice == computer_choice:
        result = "😐 It's a Draw!"
    elif (user_choice == "s" and computer_choice == "w") or \
         (user_choice == "w" and computer_choice == "g") or \
         (user_choice == "g" and computer_choice == "s"):
        result = "🎉 You Win!"
    else:
        result = "💀 You Lose!"

    label_result.config(text=f"You: {choices[user_choice]} | Computer: {choices[computer_choice]}\n{result}")

root = tk.Tk()
root.title("Snake Water Gun Game")

label_result = tk.Label(root, text="Choose your move!", font=("Arial", 16))
label_result.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

for choice in choices:
    btn = tk.Button(frame, text=choices[choice], font=("Arial", 20), command=lambda ch=choice: play(ch))
    btn.pack(side="left", padx=10)

root.mainloop()
