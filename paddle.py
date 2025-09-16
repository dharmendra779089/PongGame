from turtle import Turtle,Screen
screen = Screen()
screen.listen()

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        y += 30
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 30
        self.sety(y)

