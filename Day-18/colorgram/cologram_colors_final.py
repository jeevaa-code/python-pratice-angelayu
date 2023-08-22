import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy = Turtle()
my_screen = Screen()


# for j in range(0,10):
# timmy.setpos(x=500.00,y=10)
def postiion_change(position):
    for j in range(0, 10):
        timmy.penup()
        timmy.setx(-200)
        timmy.sety(position)
        position += 50
        for i in range(0, 10):
            random_color = random.choice(color_list)
            timmy.color(random_color)
            timmy.dot(20)

            timmy.forward(50)
        print(timmy.pos())


postiion_change(-250)
my_screen.exitonclick()
