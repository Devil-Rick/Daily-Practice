from turtle import Turtle

SCORE_POSITION = "center"
SCORE_FONT = ('Arial Black', 40, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.penup()
        self.hideturtle()
        self.color('#fff')
        self.show_score()

    def show_score(self):
        self.goto((-50, 240))
        self.write(self.p1_score, align=SCORE_POSITION, font=SCORE_FONT)
        self.goto((50, 240))
        self.write(self.p2_score, align=SCORE_POSITION, font=SCORE_FONT)

    def increase_p1(self):
        self.p1_score += 1
        self.clear()
        self.show_score()

    def increase_p2(self):
        self.p2_score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        if self.p1_score == 15 or self.p2_score == 15:
            self.goto(0, 0)
            self.write(f'GAME OVER', align=SCORE_POSITION, font=SCORE_FONT)
            if self.p1_score > self.p2_score:
                self.goto(0, -40)
                self.write(f'Player 1 Wins', align=SCORE_POSITION, font=('Arial', 30, 'normal'))
            else:
                self.goto(0, -40)
                self.write(f'Player 2 Wins', align=SCORE_POSITION, font=('Arial', 30, 'normal'))
            return True
