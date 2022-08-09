from tkinter import *
from quiz_brain import QuizBrain

# -------------- Constants --------------- #
THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = 16
FONT_STYLE = "italic"


class UserInterface:
    score = 0

    def __init__(self, quiz: QuizBrain):  # quiz(variable) : QuizBrain(Type)
        # -------------- Arguments --------------- #
        self.quiz = quiz

        # -------------- Starting Interface --------------- #
        self.root = Tk()
        self.root.title("Quiz App")
        self.root.config(bg=THEME_COLOR, pady=30, padx=30)

        # -------------- Question Image --------------- #
        self.canvas = Canvas(width=400, height=400, bg="#fff", highlightthickness=0)
        self.question = self.canvas.create_text(200, 200, text="START THE GAME",
                                                font=(FONT_NAME, FONT_SIZE, FONT_STYLE),
                                                width=350)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        # -------------- Buttons --------------- #
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img,
                               highlightthickness=0,
                               border=0,
                               command=self.button_true)
        self.true_btn.grid(row=2, column=0)

        self.start_btn = Button(text="START",command=self.start_game)
        self.start_btn.grid(row=2, column=1)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img,
                                highlightthickness=0,
                                border=0,
                                command=self.button_false)
        self.false_btn.grid(row=2, column=2)

        # -------------- Score Board --------------- #
        self.score_card = Label(text=f"Score : {self.score}",
                                bg=THEME_COLOR,
                                fg="#fff",
                                font=(FONT_NAME, FONT_SIZE))
        self.score_card.grid(row=0, column=1)

        # -------------- Starting Mainloop --------------- #
        self.root.mainloop()

    def start_game(self):
        self.next_que()
        self.start_btn.config(state="disabled")

    def next_que(self):
        self.canvas.config(bg="#fff")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.score_card.config(text=f"Score : {self.score}")
            self.canvas.itemconfig(self.question, text=next_question)
        else:
            self.canvas.itemconfig(self.question, text="Game OVER")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.start_btn.config(state="normal")

    def button_true(self):
        is_true = self.quiz.check_answer('True')
        self.feedback(is_true)

    def button_false(self):
        is_true = self.quiz.check_answer('False')
        self.feedback(is_true)

    def feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, func=self.next_que)
