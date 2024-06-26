from turtle import Turtle

STEP = 15
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.movement_speed = 0.1
        self.x_move = STEP
        self.y_move = STEP

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.movement_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self):
        self.movement_speed *= 0.9

