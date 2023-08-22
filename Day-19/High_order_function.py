'''
Turtle event listeners
'''
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

'''
In order start listeing for events 
'''


def move_forward():
    tim.forward(10)


my_screen.listen()
'''below step we are giving the function as a argument pass without parenthesis at the end 
- It is high order function'''
my_screen.onkey(key='space', fun=move_forward)
my_screen.exitonclick()
