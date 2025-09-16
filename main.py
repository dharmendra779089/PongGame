from distutils.fancy_getopt import longopt_pat   # (Not needed here, can be removed safely)
from turtle import Turtle, Screen                # Import Turtle graphics
from paddle import Paddle                        # Import Paddle class (your custom class)
from ball import Ball                            # Import Ball class (your custom class)
import time
from scoreboard import Scoreboard                # Import Scoreboard class (your custom class)

# ---------------- Setup the game screen ----------------
screen = Screen()
screen.bgcolor("black")                          # Background color black
screen.setup(width=800, height=600)              # Screen size 800x600 pixels
screen.title("Pong")                             # Window title
screen.tracer(0)                                 # Turn off auto updates (manual control for smoother animation)

# ---------------- Create game objects ----------------
l_paddle = Paddle((350, 0))                      # Create right paddle at x=350, y=0
r_paddle = Paddle((-350, 0))                     # Create left paddle at x=-350, y=0
ball = Ball()                                    # Create the ball
scoreboard = Scoreboard()                        # Create scoreboard

# ---------------- Keyboard controls ----------------
screen.listen()
screen.onkey(l_paddle.move_up, "Up")             # Right paddle moves up with "Up arrow"
screen.onkey(l_paddle.move_down, "Down")         # Right paddle moves down with "Down arrow"
screen.onkey(r_paddle.move_up, "w")              # Left paddle moves up with "W"
screen.onkey(r_paddle.move_down, "s")            # Left paddle moves down with "S"

# ---------------- Main game loop ----------------
game_on = True
while game_on:
    time.sleep(ball.move_speed)                  # Control ball speed
    screen.update()                              # Refresh screen
    ball.move()                                  # Move the ball

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:  # If ball touches top (280) or bottom (-280)
        ball.bounce_y()                          # Reverse y direction

    # Detect collision with paddles
    if (ball.distance(l_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(r_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()                          # Reverse x direction, speed up

    # Detect when right paddle misses
    if ball.xcor() > 380:                        # Ball goes out of bounds on right side
        ball.reset_position()                    # Reset ball to center
        scoreboard.l_point()                     # Left player scores a point

    # Detect when left paddle misses
    if ball.xcor() < -380:                       # Ball goes out of bounds on left side
        ball.reset_position()                    # Reset ball to center
        scoreboard.r_point()                     # Right player scores a point

# ---------------- Exit on click ----------------
screen.exitonclick()
