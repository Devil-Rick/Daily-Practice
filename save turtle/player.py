from turtle import Turtle

INITIAL_POS = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('cyan')
        self.goto(INITIAL_POS)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def restart(self):
        self.goto(INITIAL_POS)
