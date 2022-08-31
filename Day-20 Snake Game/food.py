import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Setting the food size to half the size
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")  # Setting the color to yellow
        self.speed("fastest")  # Setting the speed to fastest
        random_x = random.randint(-280, 280)  # Setting the x position of the food to a random position in X-Axis
        random_y = random.randint(-280, 280)  # Setting the y position of the food to a random position in Y-Axis
        self.goto(random_x, random_y)  # Setting the positions
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # Setting the x position of the food to a random position in X-Axis
        random_y = random.randint(-280, 280)  # Setting the y position of the food to a random position in Y-Axis
        self.goto(random_x, random_y)  # Setting the positions
