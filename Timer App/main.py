from tkinter import *
from PIL import Image, ImageTk
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BACKGROUND = "#181818"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 40
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    root.after_cancel(timer)
    head_text.config(text="Pomodoro", fg=GREEN)
    canvas.itemconfig(canvas_text, text="00:00")
    complete.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        head_text.config(text="Long Break", fg=RED)
        countdown(long_break)
        reps = 0
    elif reps % 2 == 0:
        head_text.config(text="Short Break", fg=PINK)
        countdown(short_break)
    else:
        head_text.config(text="Work Time", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer

    minute = math.floor(count / 60)
    sec = count % 60

    if minute < 10:
        minute = f"0{minute}"
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(canvas_text, text=f"{minute}:{sec}")
    if count > 0:
        timer = root.after(1000, countdown, count - 1)
    if count == 0:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        complete.config(text=mark, font=(FONT_NAME, 16))


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro Timer")  # POMODORO = TOMATO (ITALIAN)
root.configure(padx=50, pady=50, bg=BACKGROUND)

head_text = Label(text="Pomodoro", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=BACKGROUND)
head_text.grid(row=0, column=1)

canvas = Canvas(width=400, height=400, bg=BACKGROUND, highlightthickness=0)
img = Image.open("tomato.png")
img = img.resize((300, 350))
main_img = ImageTk.PhotoImage(img)
canvas.create_image(200, 200, image=main_img)
canvas_text = canvas.create_text(200, 230, text="00:00", font=(FONT_NAME, 40, "bold"), fill="#fff")
canvas.grid(row=1, column=1)

start_btn = Button(text="START", command=start_timer)
start_btn.grid(row=2, column=0, pady=20)
reset_btn = Button(text="RESET", command=reset_timer)
reset_btn.grid(row=2, column=2, pady=20)

complete = Label(text="", fg=GREEN, bg=BACKGROUND)
complete.grid(row=3, column=1)

root.mainloop()
