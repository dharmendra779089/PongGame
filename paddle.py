from turtle import Turtle, Screen

screen = Screen()
screen.listen()   # Enable listening for keyboard inputs

# ---------------- Paddle Class ----------------
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()                     # Initialize Turtle parent class
        self.shape("square")                   # Paddle shape is a square
        self.color("white")                    # Paddle color is white
        self.shapesize(stretch_wid=5, stretch_len=1)  
        # Stretch the square shape: height = 5, width = 1 → makes it look like a rectangle paddle
        self.penup()                           # Lift pen so it doesn’t draw a line when moving
        self.goto(position)                    # Place paddle at the given (x, y) position

    def move_up(self):
        y = self.ycor()                        # Get current y-coordinate of paddle
        y += 30                                # Move up by 30 pixels
        self.sety(y)                           # Update paddle’s y-coordinate

    def move_down(self):
        y = self.ycor()                        # Get current y-coordinate of paddle
        y -= 30                                # Move down by 30 pixels
        self.sety(y)                           # Update paddle’s y-coordinate
