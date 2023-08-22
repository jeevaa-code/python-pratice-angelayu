from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(key='Up', fun=snake.up)
my_screen.onkey(key='Left', fun=snake.left)
my_screen.onkey(key='Down', fun=snake.down)
my_screen.onkey(key='Right', fun=snake.right)

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.heads.distance(food) < 15:
        food.refresh()
        score.runs()
        my_screen.update()
        snake.grow()

    if snake.heads.xcor() > 290 or snake.heads.xcor() < -290 or snake.heads.ycor() > 290 or snake.heads.ycor() < -290:
        is_game_on = False
        score.gameover()

    for segments in snake.snakes_list[1:]:
        if snake.heads.distance(segments) < 10:
            is_game_on = False
            score.gameover()


my_screen.exitonclick()
