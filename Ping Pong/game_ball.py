from turtle import Turtle


class Ball(Turtle):
    y_inc = 15
    x_inc = 15  # 17

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#fff")
        self.penup()

    def move(self):
        x = self.xcor() + self.x_inc
        y = self.ycor() + self.y_inc
        self.goto(x, y)

    def bounce_y(self):
        self.y_inc *= -1

    def bounce_x(self):
        self.x_inc *= -1

    def restart(self):
        self.x_inc *= -1
        self.y_inc = 15
        self.setpos(0, 0)
