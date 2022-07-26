from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "italic")
SCORE_POS = (-400, 240)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("#fff")
        self.hideturtle()
        self.show_level()

    def show_level(self):
        self.goto(SCORE_POS)
        self.write(f"Level : {self.level}", align=ALIGN, font=FONT)

    def level_inc(self):
        self.level += 1
        self.clear()
        self.show_level()

    def gameover(self):
        self.goto(0, -50)
        self.write("GAME OVER", align=ALIGN, font=("Arial Black", 44, "bold"))
