from turtle import Turtle
from random import randrange, choice
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [250, 150, 50, -50, -150, -250]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.cars = []
        self.setup_cars()
        self.hideturtle()

    def setup_cars(self):
        for lane in LANES:
            i = 0
            while i < 4:
                car = Car(lane)
                self.cars.append(car)
                i += 1

    def cars_move(self):
        for car in self.cars:
            car.move_car()
