from turtle import Turtle

WIDTH = 20
HEIGHT = 100
RIGHT_START = (350, 0)
LEFT_START = (-350, 0)


class Paddle(Turtle):
    def __init__(self, start_location):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(RIGHT_START if start_location == 'right' else LEFT_START)

    def move_up(self):
        self.setpos(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.setpos(self.xcor(), self.ycor() - 20)

