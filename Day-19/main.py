from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Turtle move forward by 10 spaces function:
def move_forward():
    tim.forward(10)

# Listening to the space key for function move_forward:
screen.listen()
screen.onkey(key="space", fun=move_forward) #binding key with a function
screen.exitonclick()
