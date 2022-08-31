from turtle import Turtle, Screen
import time

# Declaring constants for the starting position and the move distance for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Declaring constants of the directions of the snake
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creating the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # Moving the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Function for moving the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Function for moving the snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Function for moving the snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Function for moving the snake down
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
