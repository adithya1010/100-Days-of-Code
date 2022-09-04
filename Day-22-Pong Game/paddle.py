from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")  # Changing the shape of the paddle to square
        self.color("white")  # Changing the color of the paddle to white
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor, ycor)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

# Multiplying height by 5(5x20=100) and length by 1(1x20)
# Telling the paddle to go to starting position at 350,0

