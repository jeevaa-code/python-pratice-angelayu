from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.run = 0
        self.runs()

    def runs(self):
        self.clear()
        self.write(f"score: {self.run} ", False, align="right", font=("vernada", 15, "normal"))
        self.run += 1

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over ", False, align="right", font=("vernada", 15, "normal"))
