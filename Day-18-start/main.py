import random
from turtle import *
import colorgram
# Drawing a Square:
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)


# installing modules
# import heroes
# print(heroes.gen())
# import villains
# print(villains.gen())

timmy_the_turtle = Turtle()

# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# from random import *
#
# colormode(255)
# for i in range(3, 10 + 1):
#     timmy_the_turtle.pencolor(randint(0, 255),
#                               randint(0, 255),
#                               randint(0, 255))
#     for j in range(0, i):
#         timmy_the_turtle.forward(100)
#         degree = 360 / i
#         timmy_the_turtle.right(degree)
from random import *

directions = [0, 90, 180, 270]
# colormode(255)
# timmy_the_turtle.pensize(15)
# for i in range(0, 100):
#
#     timmy_the_turtle.speed(i)
#     timmy_the_turtle.setheading(choice(directions))
#     timmy_the_turtle.pencolor(randint(0, 255),
#                               randint(0, 255),
#                               randint(0, 255))
#     timmy_the_turtle.forward(10)
# colormode(255)
# timmy_the_turtle.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         timmy_the_turtle.color(randint(0, 255),
#                                randint(0, 255),
#                                randint(0, 255))
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
#
#
# draw_spirograph(int(5))


screen = Screen()
screen.exitonclick()
