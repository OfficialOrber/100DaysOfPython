from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-300, 300)
        self.write(f'Level: {level}', align='left', font=FONT)
        self.hideturtle()

    def update_score(self, updated_level):
        self.clear()
        self.write(f'Level: {updated_level}', align='left', font=FONT)
