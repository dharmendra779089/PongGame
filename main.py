from distutils.fancy_getopt import longopt_pat
from turtle import  Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if (ball.distance(l_paddle) < 50 and ball.xcor() > 320) or (ball.distance(r_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect when  R paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    #Detect when L paddle misses
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()