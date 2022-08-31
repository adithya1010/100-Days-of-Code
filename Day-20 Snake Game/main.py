from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)  # Setting screen height and width to 600 units
screen.tracer(0)  # Setting the tracer animation off
screen.bgcolor("black")  # Setting bg color to black
screen.title("My Snake Game")  # Setting title to Snake Game

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food:
    if snake.head.distance(food) < 15:  # If distance between snake's head and food is less than 15 pixels then move
        # the food to random position
        food.refresh()
        snake.extend()
        scoreboard.increase_score()  # Increasing the Score on Scoreboard

    # Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # If head collides with any segment in tail then:
    # trigger the game over sequence

screen.exitonclick()
