import random
from turtle import Turtle,Screen

colors = ['red','yellow','green','purple','pink','orange','blue','brown','silver','gold']

tim = Turtle()
my_screen = Screen()
tim.shape("turtle")
tim.pensize(10)

while True:
    random_colors = random.choice(colors)
    Random = random.randint(0,1)
    if Random == 0:
        tim.color(random_colors)
        tim.right(90)
    else:
        tim.color(random_colors)
        tim.left(90)
    Random = random.randint(0,1)
    if Random == 0:
        tim.color(random_colors)
        tim.forward(100)
    else:
        tim.color(random_colors)
        tim.back(100)






my_screen.exitonclick()