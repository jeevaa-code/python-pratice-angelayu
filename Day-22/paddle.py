from turtle import Turtle



class Paddle(Turtle,):
    def __init__(self,position_paddle):
        super().__init__()
        self.create_paddle(position_paddle)

    def create_paddle(self, position_paddle):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.5, )
        self.penup()
        self.setposition(position_paddle, 0)

    def up(self):
        new_y = (self.ycor() + 20)
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = (self.ycor() - 20)
        self.goto(self.xcor(),new_y)
