from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # Setting screen height and width to 600 units
screen.tracer(0)  # Setting the tracer animation off
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()  # Updating the Screen
    time.sleep(0.1)  # delaying the snake by 0.1 seconds
    snake.move()


screen.exitonclick()
