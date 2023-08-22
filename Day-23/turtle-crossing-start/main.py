import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key='space', fun=player.up)

game_is_on = True
car_moving = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.random_allocation()

    if player.ycor() == player.FINISH_LINE_Y:
        player.starting_position()
        car_manager.levelup()
        scoreboard.score_up()

    for new_car in car_manager.garage:
        if player.distance(new_car) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
