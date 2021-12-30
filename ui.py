from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # sets quiz_brain to imported class data type (Type Hints)
        # super().__init__()
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz_brain
        self.new_question_text = ""

        self.score_label = Label(text="Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white", font=('arial', 10, 'bold'))
        self.score_label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(150, 125, text='Placement', width=280, font=('arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        self.get_question_text()
        self.window.mainloop()

    def get_question_text(self):
        q_text = self.quiz.next_question()
        self.canvas.configure(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.canvas.itemconfig(self.quiz_text, text=q_text)

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.get_question_text()

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.get_question_text()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_question_text)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_question_text)

