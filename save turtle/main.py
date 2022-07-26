from turtle import Screen
from player import Player
from score_board import Score
from cars import Cars
import time

screen = Screen()
#################################################
##           Screen Specifications             ##
#################################################

screen.bgcolor("#000")
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.listen()

#################################################
##           Game Specifications               ##
#################################################

player = Player()
score = Score()
car = Cars()

screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)

gameover = False
while not gameover:
    screen.update()
    time.sleep(0.1)
    car.create_cars()
    car.move()
    if player.ycor() >= 280:
        score.level_inc()
        time.sleep(0.2)
        player.restart()
        car.inc_speed()
    for current_car in car.all_cars:
        if player.distance(current_car) < 20:
            score.gameover()
            gameover = True

screen.exitonclick()
