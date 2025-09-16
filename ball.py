from turtle import Turtle, Screen   # Import Turtle (to create shapes), Screen (for window setup if needed)

class Ball(Turtle):   # Create a Ball class that inherits from Turtle
    def __init__(self):
        super().__init__()             # Initialize parent (Turtle) features
        self.shape("circle")           # Set ball shape to circle
        self.color("white")            # Set ball color to white
        self.penup()                   # Lift pen up so ball doesn’t draw lines
        self.goto(0, 0)                # Start ball at the center of the screen (0,0)
        self.x_move = 10               # Ball’s movement speed in X direction
        self.y_move = 10               # Ball’s movement speed in Y direction
        self.move_speed = 0.1          # Ball’s delay speed (lower value = faster ball)

    def move(self):  
        # Move ball by updating its x and y coordinates
        new_x = self.xcor() + self.x_move   # Current x + x_move
        new_y = self.ycor() + self.y_move   # Current y + y_move
        self.goto(new_x, new_y)             # Move ball to new position

    def bounce_y(self):
        # Reverse the Y direction when ball hits top/bottom walls
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the X direction when ball hits a paddle
        self.x_move *= -1
        self.move_speed *= 0.8   # Speed up the ball (make it faster after hitting paddle)

    def reset_position(self):
        # Reset ball to center when someone misses
        self.goto(0, 0)
        self.move_speed = 0.1    # Reset speed back to normal
        self.bounce_x()          # Send ball toward the opposite player
