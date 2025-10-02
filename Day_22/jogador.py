from turtle import Turtle


class Jogador(Turtle):
    def __init__(self, posicao_x, posicao_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posicao_x, posicao_y)

    def go_up(self):
        novo_y = self.ycor() + 20
        self.goto(self.xcor(), novo_y)

    def go_down(self):
        novo_y = self.ycor() - 20
        self.goto(self.xcor(), novo_y)