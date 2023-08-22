from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
tim.shape("turtle")


def triangle():
    for i in range(3):
        tim.right(120)
        tim.forward(100)


def square():
    tim.color('coral')
    for i in range(4):
        tim.right(90)
        tim.forward(100)


def pentagon():
    tim.color('green')
    for i in range(5):
        tim.right(72)
        tim.forward(100)
def hexagon():
    tim.color('yellow')
    for i in range(6):
        tim.right(60)
        tim.forward(100)

def heptagon():
    tim.color('red')
    for i in range(7):
        tim.right(51.42)
        tim.forward(100)
def octagon():
    tim.color('violet')
    for i in range(8):
        tim.right(45)
        tim.forward(100)
def nonagon():
    tim.color('pink')
    for i in range(9):
        tim.right(40)
        tim.forward(100)
def decagon():
    tim.color('blue')
    for i in range(10):
        tim.right(36)
        tim.forward(100)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

my_screen.exitonclick()
