from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(0,0)
        self.ball_speed = 0.1
        self.xposition = 10
        self.yposition = 10

    def move(self):
        self.penup()
        x = self.xcor() + self.xposition
        y = self.ycor() + self.yposition
        self.goto(x,y)

    def bounce(self):
        self.yposition *= -1

    def touch_paddle(self):
        self.xposition *= -1
        self.ball_speed *= 0.9

    def recontinue(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.touch_paddle()




