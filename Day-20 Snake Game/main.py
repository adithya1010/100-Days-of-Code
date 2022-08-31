from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # Setting screen height and width to 600 units
screen.tracer(0)  # Setting the tracer animation off
screen.bgcolor("black")  # Setting bg color to black
screen.title("My Snake Game")  # Setting title to Snake Game

snake = Snake()

screen.listen()  # Listening to Keystrokes
screen.onkey(key="Up", fun=snake.up)  # Binding Up key to up function in snake.py
screen.onkey(key="Down", fun=snake.down)  # Binding Down key to up function in snake.py
screen.onkey(key="Left", fun=snake.left)  # Binding Left key to up function in snake.py
screen.onkey(key="Right", fun=snake.right)  # Binding Right key to up function in snake.py

game_is_on = True
while game_is_on:
    screen.update()  # Updating the Screen
    time.sleep(0.1)  # delaying the snake by 0.1 seconds
    snake.move()  # Calling the move function in snake.py to move the snake

screen.exitonclick()
