from turtle import Turtle

MOVE_DISTANCE = 20
SCREEN_LIMIT = 250

class Paddle(Turtle):
    """Paddle controlled by a player."""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < SCREEN_LIMIT:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -SCREEN_LIMIT:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
