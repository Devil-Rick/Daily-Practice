from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

#################################################
##           Screen Specifications             ##
#################################################

screen.screensize(1000, 500, "#000")
screen.colormode(255)
screen.listen()

#################################################
##           Turtle Specifications             ##
#################################################

turtle.shape('turtle')
turtle.color("cyan")


#################################################
##           Turtle Functioning                ##
#################################################

def mv_frwd():
    turtle.fd(20)


def mv_back():
    turtle.back(20)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def sketch():
    screen.onkey(key='w', fun=mv_frwd)
    screen.onkey(key='s', fun=mv_back)
    screen.onkey(key='a', fun=turn_left)
    screen.onkey(key='d', fun=turn_right)
    screen.onkey(key='c', fun=clear)


screen.exitonclick()
