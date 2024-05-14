from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "black", "green", "blue", "pink"]
y_axis = [-120, -80, -40, 0, 40, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(-230, y_axis[turtle_index])
    all_turtles.append(new_turtle)

print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_selected in all_turtles:
        turtle_selected.forward(random.randint(0, 10))
        if turtle_selected.position()[0] > 225:
            is_race_on = False
            winning_colour = turtle_selected.pencolor()
            is_winner = 'You Won!' if winning_colour == user_bet else "You Lost!"
            print(is_winner)

screen.exitonclick()