from turtle import Turtle

SCORE_POSITION = "center"
SCORE_FONT = ('Courier', 24, 'italic')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('#fff')
        self.penup()
        self.sety(260)
        self.pendown()
        self.show_score()

    def show_score(self):
        self.write(f'SCORE : {self.score} ', align=SCORE_POSITION, font=SCORE_FONT)
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.penup()
        self.sety(0)
        self.pendown()
        self.write(f'GAME OVER', align=SCORE_POSITION, font=SCORE_FONT)
