from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title("PingPong")
my_screen.tracer(0)
Right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(key="Up", fun=Right_paddle.up)
my_screen.onkey(key="Down", fun=Right_paddle.down)
my_screen.onkey(key="w", fun=left_paddle.up)
my_screen.onkey(key="s", fun=left_paddle.down)

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(Right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.touch_paddle()
    if ball.xcor() > 370:
        ball.recontinue()
        scoreboard.l_point()
    if ball.xcor() < -370:
        ball.recontinue()
        scoreboard.r_point()

my_screen.exitonclick()
