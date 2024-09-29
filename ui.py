from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):  # must pass in a quiz_brain object of datatype 'QuizBrain'
        self.question_text = None
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)

        self.question_text = self.canvas.create_text(
            300 // 2,
            250 // 2,
            text="question_text",
            width=280,
            anchor="center",
            font=("Arial", 15, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.score_label = Label(self.window, text="Score: 0", fg="white", font=("Arial", 10, "bold"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=10, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz :)")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#80bd6a")
        else:
            self.canvas.config(bg="#e66950")
        self.window.after(1000, self.get_next_question)
