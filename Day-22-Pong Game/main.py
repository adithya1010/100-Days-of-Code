# TODO 1: Create the Screen
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)  # Setting the width of the screen to 800 and height of the screen to 600
screen.bgcolor("black")  # Setting the background color of the screen to black
screen.title("Pong Game")  # Setting the title of the game to "Pong Game"
screen.tracer(0)
# TODO 2: Create a paddle that responds to key presses


# TODO 3: Create paddle class and pass in just the coordinates to create a new paddle
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
screen.listen()
screen.onkey(fun=left_paddle.move_up, key='w')
screen.onkey(fun=left_paddle.move_down, key='s')
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')

# TODO 4: Create the ball class and make it move


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 7: Detect when ball misses the paddles and reset the ball
    # Detect collision with the right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

    # Detect collision with the left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()

    # TODO 6: Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

screen.exitonclick()  # Allowing the game to exit on click on the screen
