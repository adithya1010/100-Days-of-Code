from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Turtle move forward by 10 spaces function:
def move_forward():
    tim.forward(10)


# Turtle move backward by 10 spaces function:
def move_backward():
    tim.backward(10)


# Turtle move right by 10 degrees function:
def turn_right():
    tim.right(10)


# Turtle move left by 10 degrees function:
def turn_left():
    tim.left(10)


# Turtle clear and reset at starting position function:
def clear_and_reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Listening to keystrokes:
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)

screen.onkey(key="c", fun=clear_and_reset)

screen.exitonclick()
