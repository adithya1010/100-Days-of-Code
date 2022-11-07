THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # canvas
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)  # Specify image height and width in the
        # Question text
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating the right_button and placing it using grid system
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # Creating the wrong_button and placing it using grid system
        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        # Step 2: Creating a Canvas
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Function for true button
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    # Function for false button
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
