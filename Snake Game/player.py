from turtle import Turtle


class Player(Turtle):

    #################################################
    ##           Turtle Specifications             ##
    #################################################

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.goto(self.position)
        self.setheading(90)
        self.shape('square')
        self.color('cyan')
        self.turtlesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
