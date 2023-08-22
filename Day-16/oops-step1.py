'''
class - blueprint
from this blueprint we can create the object..
CarBlueprint is a class
car is a object
car = CarBlueprint()

'''
import another_module
from another_module import another_variable

z = another_module.another_variable
y = another_module.another_method()
a = another_variable
print(z)

import turtle

thio = turtle.Turtle()

from turtle import Turtle,Screen

ajith = Turtle()
my_screen = Screen()
thio.shape("turtle")
thio.color("azure4")
thio.forward(100)
print(my_screen.canvheight)
my_screen.exitonclick()

'''
object attributes
car has attribute speed = 0 , fuel = 32.
to access attribute
car.speed = 0
'''
'''
def move():
   speed = 60

def stop():
   speed = 0
car.stop()
'''

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charizard", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)

