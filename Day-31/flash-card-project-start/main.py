BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

to_learn = {}
# Reading the French words csv
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # try to read from to_learn.csv
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")  # If file is not found then read French words
    to_learn = original_data.to_dict(orient="records")  # to_learn becomes the original data
else:
    to_learn = data.to_dict(orient="records")  # Orders elements row-wise else to_learn becomes words_to_learn

current_card = ""


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")  # Set card title
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  # Set card word to current
    canvas.itemconfig(canvas_image, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


# This function is going to remove the known card from the list
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Step 1: Creating a Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Step 2: Creating a Canvas
canvas = Canvas(height=526, width=800, highlightthickness=0)  # Specify image height and width in the canvas
card_front_img = PhotoImage(file="./images/card_front.png")  # Tkinter uses PhotoImage to get and store images in a
# variable
card_back_img = PhotoImage(file="./images/card_back.png")  # Tkinter uses PhotoImage to get and store images in a
canvas_image = canvas.create_image(400, 263, image=card_front_img)  # Image needs to be positioned at the center of
# the canvas
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Title Label
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))

# Word Label
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Creating the wrong_button and placing it using grid system
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Creating the right_button and placing it using grid system
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()  # Calling the next card function

window.mainloop()
