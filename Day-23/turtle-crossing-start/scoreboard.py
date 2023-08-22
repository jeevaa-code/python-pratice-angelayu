from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.color("black")
        self.penup()
        self.goto(-220, +250)
        self.hideturtle()
        self.level = 1
        self.score_board()

    def score_board(self):
        self.write(f"level: {self.level}", False, align="center", font=FONT)

    def score_up(self):
        self.clear()
        self.level += 1
        self.score_board()

    def game_over(self):
        self.goto(0,0)
        self.write(f"gameover", False, align="center", font=FONT)

