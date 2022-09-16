import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# 1: Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the
# turtle north.
screen.listen()
screen.onkey(fun=player.move_up, key="Up")

# 2: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the
# left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a
# safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs

# 3: Detect when the turtle player collides with a car and stop the game if this happens.
# 4: Detect when the
#  turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens,
#  return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an
#  attribute and using the MOVE_INCREMENT to increase the car speed

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        if player.check_finish():
            car_manager.level_up()
            scoreboard.level_up()

screen.exitonclick()
