import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.cars_move()
    if player.ycor() >= player.finish_line:
        player.reset_position()
    screen.update()

