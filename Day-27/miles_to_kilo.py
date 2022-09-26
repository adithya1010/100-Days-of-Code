from tkinter import *

window = Tk()  # Creating a tkinter object for window

window.title("Miles to KM Converter")  # Setting the title for the window
window.minsize(width=500, height=300)


def calculate():
    miles_input = int(miles_entry.get())
    km_answer = int(miles_input * 1.6)
    result_label.config(text=str(km_answer))


miles_entry = Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)
window.mainloop()
