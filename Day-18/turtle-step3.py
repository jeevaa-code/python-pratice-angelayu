from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
tim.shape("turtle")
colors = ['red','yellow','green','purple','pink','orange','blue','brown','silver','gold']


def shapes(sides):
    for i in range(sides):
        angle = 360 / sides
        tim.right(angle)
        tim.forward(100)


color_no = 0
for i in range(3, 11):
    tim.color(colors[color_no])
    shapes(i)
    color_no += 1


my_screen.exitonclick()
