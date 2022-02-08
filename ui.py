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
        self.true_btn = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, bd=0,
                               command=self.true_pressed)
        self.true_btn.grid(column=0, row=2, padx=20, pady=20, sticky="e")
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, bd=0,
                                command=self.false_pressed)
        self.false_btn.grid(column=1, row=2, padx=20, pady=20, sticky="w")

        # Initializing next question
        self.get_next_question()

        # Mainloop
        self.window.mainloop()

    # looping through questions
    def get_next_question(self):
        self.scoreboard.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text=f"End of the quiz.\nYour score is {self.quiz.score}/10.")
            self.buttons_state(DISABLED)

    # True button pressed
    def true_pressed(self):
        self.buttons_state(DISABLED)
        self.give_feedback(self.quiz.check_answer("True"))

    # False button pressed
    def false_pressed(self):
        self.buttons_state(DISABLED)
        self.give_feedback(self.quiz.check_answer("False"))

    # giving feedback
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    # Disabling / enabling button use
    def buttons_state(self, state):
        self.true_btn.config(state=state)
        self.false_btn.config(state=state)

