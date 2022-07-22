from turtle import Turtle, Screen
import random as rn

colors = ["red", "yellow", "white", "pink", "orange", "blue", "green"]
y = 0
all_t = []

#################################################
##           Screen Specifications             ##
#################################################
screen = Screen()
screen.screensize(500, 500, "#000")
screen.colormode(255)
screen.listen()
screen.setworldcoordinates(-2, -1, screen.window_width() - 1, screen.window_height() - 1)

#################################################
##           Turtle Specifications             ##
#################################################

c_list = '\n'.join(colors)
bet = screen.textinput(title="Make you BET", prompt=f"Which turtle is gonna win ? Pick a Color: \n{c_list}")

for i in range(7):
    turtle = Turtle()
    turtle.penup()
    turtle.shape('turtle')
    turtle.color(colors[i])
    turtle.sety(y)
    all_t.append(turtle)
    y += 100

race = False
if bet:
    race = True

while race:
    for turtle in all_t:
        turtle.forward(rn.randint(1, 20))
        if turtle.xcor() > 750:
            if turtle.pencolor() == bet:
                print(f"{turtle.pencolor()} Good Choice. You have won")
            else:
                print(f"{turtle.pencolor()} is the Winner. You have lost")
            race = False





#################################################
##           Turtle Functioning                ##
#################################################
screen.exitonclick()
