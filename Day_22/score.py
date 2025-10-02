from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pontos_1 = 0
        self.pontos_2 = 0
        self.goto(-100, 200)
        self.write(self.pontos_2, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.pontos_1, align="center", font=("courier", 80, "normal"))

    def ponto_jogador_1(self):
        self.pontos_1 += 1

    def ponto_jogador_2(self):
        self.pontos_2 += 1

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.pontos_2, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.pontos_1, align="center", font=("courier", 80, "normal"))