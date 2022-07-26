from turtle import Screen
from player import Player
from game_ball import Ball
from score_board import Score
import time

screen = Screen()

#################################################
##           Screen Specifications             ##
#################################################

screen.bgcolor('#000')
screen.setup(width=1000, height=600)
screen.listen()
screen.title("PING PONG GAME")
screen.tracer(0)

#################################################
##           Game Functioning                ##
#################################################
player1 = Player((-480, 0))
player2 = Player((480, 0))
ball = Ball()
score = Score()

screen.onkey(fun=player1.up, key="w")
screen.onkey(fun=player1.down, key="s")
screen.onkey(fun=player2.up, key="Up")
screen.onkey(fun=player2.down, key="Down")

gameover = False
while not gameover:
    screen.update()
    ball.move()
    time.sleep(ball.time)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(player2) < 50 and ball.xcor() > 450) or (ball.distance(player1) < 50 and ball.xcor() < -450):
        ball.bounce_x()

    if ball.xcor() > 480:
        score.increase_p1()
        ball.restart()
    elif ball.xcor() < -480:
        score.increase_p2()
        ball.restart()

    if score.game_over():
        gameover = True


screen.exitonclick()
