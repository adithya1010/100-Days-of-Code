from tkinter import *

window = Tk()  # Creating a tkinter object for window

window.title("My first GUI program")  # Setting the title for the window
window.minsize(width=500, height=300)  # Setting the min size for the window
window.config(padx=100, pady=200)
# Creating a Label:
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# Displaying the label using pack:
my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
my_label["text"] = "New Text"


# Button
def button_clicked():
    print("I got clicked")
    user_input = input.get()  # The get function gets the input that's entered in the entry box
    my_label.config(text=user_input)


button = Button(text="Click Me", command=button_clicked)  # Creating a button with text-"Click Me" and listening to
# function - button_clicked
 # Packing and displaying the button
button.grid(column=1, row=1)
# Entry - input text box
new_button = Button(text="New button")
new_button.grid(column=2, row=0)
input = Entry(width=10)  # Creates an Entry box with width 10
input.grid(column=3, row=2)
window.mainloop()
