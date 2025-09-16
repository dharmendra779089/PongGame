from turtle import Turtle

# ---------------- Scoreboard Class ----------------
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()            # Initialize the Turtle parent class
        self.color("white")           # Text color is white
        self.penup()                  # Lift pen so no lines are drawn
        self.hideturtle()             # Hide the turtle shape, we only want text
        self.l_score = 0              # Start left player’s score at 0
        self.r_score = 0              # Start right player’s score at 0
        self.update_scoreboard()      # Show the initial score on the screen

    def update_scoreboard(self):
        self.clear()                  # Clear old score before writing new one
        self.goto(-100, 200)          # Move to left side of the screen
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Write left player's score in big font
        self.goto(100, 200)           # Move to right side of the screen
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        # Write right player's score

    def l_point(self):
        self.l_score += 1             # Add 1 point to left player
        self.update_scoreboard()      # Refresh scoreboard to show new score

    def r_point(self):
        self.r_score += 1             # Add 1 point to right player
        self.update_scoreboard()      # Refresh scoreboard to show new score
