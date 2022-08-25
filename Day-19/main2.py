from turtle import Turtle, Screen
import random
screen = Screen()

# Setting width and height to the screen of the game
screen.setup(width=500, height=400)
# Getting the bet for the race by using textinput
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
go_up = 30
y_position = -100
is_race_on = False

# Creating six Turtles
for i in range(0, 6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    y_position += go_up
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)

# When user bet is on the race is on
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Each turtle is 40 by 40 so when its head is over 230 then we declare it as the winner
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # if the user bet is equal to the color of the winning turtle then we print yes else no for winner
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the winner is {winning_color} turtle")
        # incrementing each turtle by a random distance from 0 to 10
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





# exiting screen on click
screen.exitonclick()
