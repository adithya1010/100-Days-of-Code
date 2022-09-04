# TODO 8: Create a scoreboard class and increase score for respective paddles

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    # Function that adds point to the score to the left board when right paddle misses and update the screen
    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    # Function that adds point to the score to the right board when right paddle misses and update the screen
    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
