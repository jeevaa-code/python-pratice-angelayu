from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# positions = [(300, -240), (300, -210), (300, -190), (300, -170), (300, -140), (300, -110), (300, -90)]

MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.new_car = None
        self.garage = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_car(self):
        random_number = random.randint(1,6)
        if random_number == 1:
            new_turtle = Turtle()
            new_turtle.shape('square')
            new_turtle.shapesize(stretch_wid=0.75, stretch_len=2)
            new_turtle.penup()
            new_turtle.goto(300, random.randint(-250, 250))
            new_turtle.color(random.choice(COLORS))
            self.garage.append(new_turtle)

    # def moving(self):
    # self.back(STARTING_MOVE_DISTANCE)

    def random_allocation(self,):
        for self.new_car in self.garage:
            self.new_car.back(self.STARTING_MOVE_DISTANCE)

    def levelup(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.random_allocation()


