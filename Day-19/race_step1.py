from turtle import Turtle,Screen
import random

is_true = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_choice = my_screen.textinput(title='Make your bet',prompt='Which Turtle will win the race? Which color ?')
colors = ['red','blue','green','yellow','orange','violet']
turtles = []

y = -100
for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(-230, y)
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    y += 40


if (user_choice):
    is_true = True


while is_true:
    for new_turtle in turtles:
        if new_turtle.xcor() > 230:
            is_true = False
            wining_horse = new_turtle.pencolor()
            if user_choice == wining_horse :
                print(f"you've won! the {wining_horse} turtle is the winner")
            else:
                print(f"you've loss! the {wining_horse} turtle is the winner")
        speed = random.randint(0, 10)
        new_turtle.forward(speed)


my_screen.exitonclick()