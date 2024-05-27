from turtle import Turtle
from random import randrange, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [250, 150, 50, -50, -150, -250]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.setup_cars()

    def setup_cars(self):
        for lane in LANES:
            i = 0
            while i < 4:
                new_car = Turtle()
                new_car.penup()
                new_car.shape('square')
                new_car.shapesize(1.5, 3)
                new_car.setheading(180)
                new_car.color(choice(COLORS))
                new_car.goto(randrange(-250, 250, 10), lane)
                self.all_cars.append(new_car)
                i += 1

    def reset_if_at_edge(self, car):
        if car.xcor() <= -380:
            car.goto(randrange(300, 350), car.ycor())

    def cars_move(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)
            self.reset_if_at_edge(car)
