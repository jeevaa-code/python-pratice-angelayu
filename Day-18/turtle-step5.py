import random
import turtle

from turtle import Turtle, Screen


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


turtle.colormode(255)
directions = [0, 90, 180, 270]
tim = Turtle()
my_screen = Screen()

tim.shape("turtle")
tim.pensize(10)


while True:
    random_direction = random.choice(directions)
    tim.color(colors())
    tim.setheading(random_direction)
    tim.forward(50)
