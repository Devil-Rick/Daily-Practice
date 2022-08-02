from tkinter import *
import math


def convert():
    result['text'] = f"{math.ceil(int(miles.get()) * 1.61)} Kms."


root = Tk()
root.geometry("1000x500")
root.title('Simple Miles Convertor')
root.configure(padx=100, pady=50, bg="cyan")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


mainframe = Frame(root, bg="cyan")
mainframe.grid(row=0, column=0, sticky="NESW")
mainframe.grid_rowconfigure(10, weight=1)
mainframe.grid_columnconfigure(10, weight=1)

label_miles = Label(mainframe, text="Enter the Miles: ", bg="cyan", font=("Times New Roman", 24, 'italic'))
label_miles.grid(row=0, column=0, padx=(100, 0))

text = StringVar()
miles = Entry(mainframe, textvariable=text, font=("Times New Roman", 24, 'italic'))
miles.grid(row=0, column=1)

b1 = Button(mainframe, text="Convert MILES", command=convert)
b1.grid(row=1, column=1, pady=50, padx=(0, 300))

result = Label(mainframe, text="0 Kms.", font=("Times New Roman", 40, 'italic'), bg="cyan")
result.place(x=250, y=150)

root.mainloop()
