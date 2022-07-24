from turtle import Turtle
import random as rn


class Food(Turtle):
    def __init__(self):
        super().__init__()  # inherits the turtle class
        self.shape('circle')
        self.penup()
        self.shapesize(0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = rn.randint(-280, 280)
        y = rn.randint(-280, 260)
        self.goto(x, y)
