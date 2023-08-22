from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def counter_clockwise():
    tim.setheading(tim.heading() + 10)



def clockwise():
    tim.setheading(tim.heading() - 10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



my_screen.listen()
my_screen.onkey(key='w', fun=move_forward)
my_screen.onkey(key='s', fun=move_backward)
my_screen.onkey(key='a', fun=counter_clockwise)
my_screen.onkey(key='d',fun=clockwise)
my_screen.onkey(key='c',fun=clear_drawing)


my_screen.exitonclick()
