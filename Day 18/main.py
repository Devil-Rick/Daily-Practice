from turtle import Turtle, Screen
import random as rn
import colorgram as cl

turtle = Turtle()
screen = Screen()

#################################################
##           Screen Specifications             ##
#################################################

screen.screensize(1000, 500, "#000")
screen.colormode(255)

#################################################
##           Turtle Specifications             ##
#################################################

turtle.shape('turtle')
turtle.color("cyan")


#################################################
##           Turtle Functioning                ##
#################################################
def random_color():
    r = rn.randint(0, 255)
    g = rn.randint(0, 255)
    b = rn.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_walk():
    for _ in range(200):
        angle = rn.choice([90, 180, 270, 0])
        turtle.speed(10)
        turtle.pensize(6)
        turtle.color(random_color())
        turtle.setheading(angle)
        turtle.forward(30)


def spirograph(angle):
    for _ in range(int(360/angle)):
        turtle.speed(15)
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + angle)


def hirst_painting():
    extract = cl.extract("Image.jpg", 30)
    colours = []
    for i in extract:
        rgb_cl = i.rgb
        rgb = (rgb_cl[0], rgb_cl[1], rgb_cl[2])
        colours.append(rgb)
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(15)
    y = -250
    turtle.setpos(-250, y)
    for i in range(15):
        for _ in range(15):
            turtle.pendown()
            turtle.dot(20, rn.choice(colours))
            turtle.penup()
            turtle.fd(30)
        y += 30
        turtle.setpos(-250, y)


hirst_painting()

screen.exitonclick()
