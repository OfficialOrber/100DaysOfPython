import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.listen()

car_speed = 0.1

player = Player()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard(1)

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    car_manager.cars_move()
    if player.ycor() >= player.finish_line:
        player.reset_position()
        player.level_up()
        scoreboard.update_score(player.level)
        car_speed *= 0.8

    for car in car_manager.all_cars:
        if car.distance(player) < 50:
            game_is_on = False
            scoreboard.goto(-50, 0)
            scoreboard.write('Game Over!', align='left', font=("Courier", 24, "normal"))
    screen.update()

screen.exitonclick()