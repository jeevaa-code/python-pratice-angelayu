from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
timmy.color('coral')
timmy.shape("turtle")


def square():
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
    timmy.forward(5)

for i in range(20):
    square()

my_screen.exitonclick()
