FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.level = 0
        self.update()

    def level_up(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level:{self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")

