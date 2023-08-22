from turtle import Turtle

RIGHT = 0
UP = 90
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.heads = self.snakes_list[0]

    def create_snake(self):
        x = 0
        for i in range(0, 3):
            new_turtle = Turtle("square")
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(x, 0)
            self.snakes_list.append(new_turtle)
            x -= 20

    def grow(self):
        new_turtle = Turtle("square")
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(self.snakes_list[-1].position())
        self.snakes_list.append(new_turtle)



    def move(self):
        for i in range(len(self.snakes_list) - 1, 0, -1):
            new_x = self.snakes_list[i - 1].xcor()
            new_y = self.snakes_list[i - 1].ycor()
            self.snakes_list[i].goto(new_x, new_y)
        self.snakes_list[0].forward(20)
        self.heads.speed("fastest")



    def right(self):
        if self.heads.heading() != LEFT:
            self.heads.setheading(RIGHT)

    def up(self):
        if self.heads.heading() != DOWN:
            self.heads.setheading(UP)

    def down(self):
        if self.heads.heading() != UP:
            self.heads.setheading(DOWN)

    def left(self):
        if self.heads.heading() != RIGHT:
            self.heads.setheading(LEFT)
