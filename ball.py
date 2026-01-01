from turtle import Turtle

STARTING_MOVE_DISTANCE = 10
MOVE_ACCELERATION = 0.9

class Ball(Turtle):
    """Ball that moves and bounces in the Pong game."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.x_move = STARTING_MOVE_DISTANCE
        self.y_move = STARTING_MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= MOVE_ACCELERATION

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
