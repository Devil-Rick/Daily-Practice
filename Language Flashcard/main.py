from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import random as rn

# ------------------- CONSTANTS ------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = ["Courier", "Arial Black"]
FONT_SIZE = [32, 36]
FILL_COLOR = "#fff"

# ------------------- DATA ACQUIRING ------------------- #
game = False
data = pd.read_csv("./data/french_words.csv")
correct_guess = []


# ------------------- GUESS CORRECT ------------------- #
def guess_correct():
    if game:
        canvas.itemconfig(img, image=card_front)
        root.after_cancel(timer)
        next_card()
        correct_guess.append(question)


# ------------------- GUESS WRONG ------------------- #
def guess_wrong():
    if game:
        canvas.itemconfig(img, image=card_front)
        root.after_cancel(timer)
        next_card()


# ------------------- PLAY GAME ------------------- #
def start_game():
    global game, correct_guess
    if not game:
        start.config(text="STOP")
        next_card()
        game = True
    else:
        root.after_cancel(timer)
        start.config(text="START")
        canvas.itemconfig(img, image=card_front)
        canvas.itemconfig(word, fill="#000", text="WORD")
        canvas.itemconfig(title, fill="#000", text="LANGUAGE")
        correct_guess = []
        game = False


# ------------------- MAIN CANVAS ------------------- #
def change_canvas():
    canvas.itemconfig(img, image=card_back)
    canvas.itemconfig(word, fill=FILL_COLOR, text=data.iloc[question]["English"])
    canvas.itemconfig(title, fill=FILL_COLOR, text="ENGLISH")


# ------------------- CHANGE CARD ------------------- #
def next_card():
    global question, timer
    question = rn.randint(0, 100)
    if question not in correct_guess:
        canvas.itemconfig(title, fill="#000", text="FRENCH")
        canvas.itemconfig(word, fill="#000", text=data.iloc[question]["French"])
        timer = root.after(3000, func=change_canvas)


# ------------------- USER INTERFACE ------------------- #
root = Tk()
root.config(bg=BACKGROUND_COLOR, pady=30, padx=30)
root.title("FRENCH Flash Card")

card_front = Image.open("./images/card_front.png")
card_front = card_front.resize((600, 350))
card_front = ImageTk.PhotoImage(card_front)

card_back = Image.open("./images/card_back.png")
card_back = card_back.resize((600, 350))
card_back = ImageTk.PhotoImage(card_back)

canvas = Canvas(width=700, height=400,
                highlightthickness=0,
                bg=BACKGROUND_COLOR)
img = canvas.create_image(350, 200, image=card_front)
title = canvas.create_text(350, 160, text="LANGUAGE",
                           font=(FONT_NAME[0], FONT_SIZE[0]))
word = canvas.create_text(350, 220, text="WORD",
                          font=(FONT_NAME[1], FONT_SIZE[1]))
canvas.grid(row=0, column=0, columnspan=3)

btn_right = Image.open("./images/right.png")
btn_right = btn_right.resize((80, 80))
btn_right = ImageTk.PhotoImage(btn_right)

btn_wrong = Image.open("./images/wrong.png")
btn_wrong = btn_wrong.resize((80, 80))
btn_wrong = ImageTk.PhotoImage(btn_wrong)

right = Button(image=btn_right, border=0,
               highlightthickness=0, command=guess_correct)
right.grid(row=1, column=0)

start = Button(text="START", command=start_game)
start.grid(row=1, column=1)

wrong = Button(image=btn_wrong, border=0,
               highlightthickness=0, command=guess_wrong)
wrong.grid(row=1, column=2)

root.mainloop()
