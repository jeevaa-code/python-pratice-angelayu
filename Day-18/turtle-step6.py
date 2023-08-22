import turtle
from turtle import Turtle
import random

tim = Turtle()
turtle.colormode(255)


def colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color

def draw_graph(set_value):
    for i in range(int(360/set_value)):
        tim.color(colors())
        tim.circle(100)
        tim.setheading(tim.heading() + set_value)

draw_graph(5)

