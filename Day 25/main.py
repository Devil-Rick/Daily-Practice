import pandas as pd
from turtle import Screen, Turtle

#################################################
##           Screen Specifications             ##
#################################################

screen = Screen()
screen.title("US-States Game")
screen.bgcolor("#000")
screen.addshape("blank_states_img.gif")
screen.setup(width=800, height=600)

#################################################
##           Turtle Specifications             ##
#################################################

turtle = Turtle()
turtle.shape("blank_states_img.gif")

#################################################
##           Turtle Funtioning                 ##
#################################################


def write_name(pos, s_name):
    tur_write = Turtle()
    tur_write.penup()
    tur_write.hideturtle()
    tur_write.goto(pos)
    tur_write.write(s_name, font=("Courier", 12, "normal"))


states = []
df = pd.read_csv("50_states.csv")
while len(states) != 50:
    answer = screen.textinput(title=f"Correct Answer: {len(states)}/50 ", prompt="Name a State :").title()
    for c_answer in df['state']:
        if c_answer == answer:
            cor = (int(df[df["state"] == c_answer]["x"]), int(df[df["state"] == c_answer]["y"]))
            write_name(cor, c_answer)
            states.append(c_answer)

screen.mainloop()
