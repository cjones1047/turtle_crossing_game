from turtle import Turtle

STARTING_POSITION = (0, -280)
STARTING_DIRECTION = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line_y = FINISH_LINE_Y
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.set_starting_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def set_starting_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(STARTING_DIRECTION)
