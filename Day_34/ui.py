import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = tkinter.Label(
            text="Score: 0", fg="white", background=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        imagem_sim = tkinter.PhotoImage(file=r"Day_34\images\true.png")
        self.butao_verdadeiro = tkinter.Button(image=imagem_sim, highlightthickness=0, command=self.pressionou_verdade)
        self.butao_verdadeiro.grid(row=2, column=0)

        imagem_nao = tkinter.PhotoImage(file=r"Day_34\images\false.png")
        self.butao_falso = tkinter.Button(image=imagem_nao, highlightthickness=0, command=self.pressionou_falso)
        self.butao_falso.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Você já respondeu a todas as perguntas")
            self.butao_verdadeiro.config(state="disabled")
            self.butao_falso.config(state="disabled")

    def pressionou_verdade(self):
        acertou = self.quiz.check_answer("True")
        self.give_feedback(acertou)

    def pressionou_falso(self):
        acertou = self.quiz.check_answer("False")
        self.give_feedback(acertou)

    def give_feedback(self, acertou):
        if acertou:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)