from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random as rn
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND = "#fffa8d"
FONT_NAME = "Arial"
FONT_SIZE = [12, 24, 40]
A_Z = range(65, 91)
a_z = range(97, 123)
NUMBERS = range(48, 57)
SPECIAL = ["!", "@", "#", "$", "%", "&"]
PASS_CHAR = [A_Z, a_z, NUMBERS, SPECIAL]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    total_characters = rn.randint(8, 14)
    password_final = ""
    for _ in range(total_characters):
        char = rn.randint(0, 3)
        if char == 3:
            password_final += rn.choice(SPECIAL)
        else:
            character = rn.choice(PASS_CHAR[char])
            password_final += chr(character)
    password_entry.delete(0, END)
    password_entry.insert(0, password_final)
    pyperclip.copy(password_final)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(website_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Invalid Input", message="All the columns are necessary", icon="error")
    else:
        is_ok = messagebox.askokcancel(title="Confirm",
                                       icon="warning",
                                       message=f"Check the details:\nWebsite: {website_entry.get()}\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_entry.get()} || {email_entry.get()} || {password_entry.get()}\n")
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Generator")
root.config(bg=BACKGROUND, padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
img = Image.open("logo.png")
main_img = ImageTk.PhotoImage(img)
canvas_img = canvas.create_image(100, 100, image=main_img)
canvas.grid(row=0, column=1)

website_name = Label(text="Website Name  ", font=(FONT_NAME, FONT_SIZE[0]), bg=BACKGROUND)
website_name.grid(row=1, column=0)
website_entry = Entry(textvariable=StringVar(), width=70)
website_entry.grid(row=1, column=1, columnspan=2)

email = Label(text="Email/Username  ", font=(FONT_NAME, FONT_SIZE[0]), bg=BACKGROUND)
email.grid(row=2, column=0, pady=10)
email_entry = Entry(textvariable=StringVar(), width=70)
email_entry.insert(0, "any_email@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password  ", font=(FONT_NAME, FONT_SIZE[0]), bg=BACKGROUND)
password.grid(row=3, column=0, pady=(0, 10))
password_entry = Entry(textvariable=StringVar(), width=51)
password_entry.grid(row=3, column=1)

btn_gen_pass = Button(text="Generate Password", command=pass_generator)
btn_gen_pass.grid(row=3, column=2)

btn_add = Button(text="Add", width=60, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

root.mainloop()
