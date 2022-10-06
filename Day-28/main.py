from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")    # title_label "Timer"
    # reset check_marks
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # Converting minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Every 8th rep is a long break
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", font=("Arial", 24, "bold"), bg=YELLOW, fg=RED)
    # Every second rep is a short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", font=("Arial", 24, "bold"), bg=YELLOW, fg=PINK)
    # Every odd rep is a working time
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # The floor function removes values after the decimal point
    count_sec = count % 60  # Getting the remainder as seconds
    if count_sec < 10:
        count_sec = "0" + str(
            count_sec)  # Dynamically changing the data type of count_sec to display 00:00 instead of 0

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        # No of work sessions is equal to reps/2
        # For every completed work completed add a check mark
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Creating a Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Tkinter uses PhotoImage to get and store images in a variable
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
check_marks = Label(bg=YELLOW, fg=GREEN, font=("Arial", 24, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
