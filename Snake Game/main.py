from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()

#################################################
##           Screen Specifications             ##
#################################################

screen.bgcolor("#000")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.title("Feed THE Snake")
screen.tracer(0)
screen.listen()

#################################################
##           Snake Game Functioning            ##
#################################################


# Start Game
snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

stop = False
while not stop:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_snake()
        score.increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 260 or snake.head.ycor() < -290:
        stop = True
        score.game_over()

    for snake_tail in snake.snake_body[1:]:
        if snake.head.distance(snake_tail) < 10:
            stop = True
            score.game_over()


screen.exitonclick()
