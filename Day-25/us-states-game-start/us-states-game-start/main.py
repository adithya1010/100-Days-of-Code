from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

# Setting the screen and turtle to shape as the image of US
screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
correct_counter = 0
while correct_counter != 50:
    # Getting the guess of the user in a variable and capitalizing every first letter of each word
    answer_state = screen.textinput(title=f"{correct_counter}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state in states_list:
        write_turtle = Turtle()
        write_turtle.hideturtle()
        write_turtle.penup()
        # Getting the details of the correct state guessed and storing it in state_data
        state_data = states_data[states_data.state == answer_state]
        # Getting the x and y position of the state to be printed on screen
        x_position = int(state_data.x)
        y_position = int(state_data.y)
        # Writing the name of the state on screen
        write_turtle.goto(x_position, y_position)
        write_turtle.write(answer_state)
        # Incrementing the counter for every correct answer and printing it in the title of the input prompt
        correct_counter += 1

screen.mainloop()
