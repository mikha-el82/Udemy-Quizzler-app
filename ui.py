from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score
        self.scoreboard = Label(text="Score: 0", font="Arial 10 bold", fg="white", bg=THEME_COLOR)
        self.scoreboard.grid(column=1, row=0, padx=20, pady=20)
        # Question canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Question", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, bd=0)
        self.true_btn.grid(column=0, row=2, padx=20, pady=20, sticky="e")
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, bd=0)
        self.false_btn.grid(column=1, row=2, padx=20, pady=20, sticky="w")

        # Initializing next question
        self.get_next_question()

        # Mainloop
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

