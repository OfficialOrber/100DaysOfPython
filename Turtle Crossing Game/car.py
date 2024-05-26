from turtle import Turtle
from random import randrange, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self, lane):
        super().__init__()
        self.hideturtle()
        self.new_car = Turtle()
        self.new_car.penup()
        self.new_car.shape('square')
        self.new_car.shapesize(1.5, 3)
        self.new_car.setheading(180)
        self.new_car.color(choice(COLORS))
        self.new_car.goto(randrange(-250, 250, 10), lane)

    def move_car(self):
        self.new_car.forward(MOVE_INCREMENT)
        if self.new_car.xcor() <= -350:
            self.new_car.goto(350, self.new_car.ycor())
