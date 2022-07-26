from turtle import Turtle
import random as rn

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
SPEED_INC = 5


class Cars:
    def __init__(self):
        self.all_cars = []
        self.mv_speed = MOVE_DISTANCE
        # self.inc_speed()

    def create_cars(self):
        create_true = rn.randint(1,6)
        if create_true == 1:
            y_axis = rn.randint(-260, 260)
            n_car = Turtle()
            n_car.shape("square")
            n_car.penup()
            n_car.turtlesize(stretch_wid=1, stretch_len=2)
            n_car.color(rn.choice(COLORS))
            n_car.goto(500, y_axis)
            self.all_cars.append(n_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.mv_speed)

    def inc_speed(self):
        self.mv_speed += SPEED_INC
