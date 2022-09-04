# TODO 4: Create the ball class and make it move
from turtle import Turtle, Screen

screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # TODO 5: Detect Collision with the wall and bounce
    def bounce_y(self):
        self.y_move *= -1  # Changing the coordinate of the y-axis to the opposite direction
        self.move_speed *= 0.9

    # Bouncing in the X direction
    def bounce_x(self):
        self.x_move *= -1  # Changing the direction of the x-axis to the opposite direction
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
