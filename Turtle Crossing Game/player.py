from turtle import Turtle

STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y
        self.level = 1

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        self.level += 1
