from turtle import Turtle

X_CORR_INITIAL = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    len_snake = 3

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    #################################################
    ##           Turtle Specifications             ##
    #################################################

    # Creating the snake Body
    def create_snake(self):
        for pos in X_CORR_INITIAL:
            self.add_snake(pos)

    def add_snake(self, pos):
        turtle = Turtle('square')
        turtle.color("cyan")
        turtle.penup()
        turtle.goto(pos)
        self.snake_body.append(turtle)

    #################################################
    ##           Turtle Functioning                ##
    #################################################

    # Increasing size of snake
    def increase_snake(self):
        self.add_snake(self.snake_body[-1].position())

    # Moving the snake
    def move_snake(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            x = int(self.snake_body[i - 1].xcor())
            y = int(self.snake_body[i - 1].ycor())
            self.snake_body[i].goto(x, y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
