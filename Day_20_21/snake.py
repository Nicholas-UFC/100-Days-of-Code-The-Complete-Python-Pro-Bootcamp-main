from turtle import Turtle

POSICAO_INICIAL = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_QUE_SE_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self) -> None:
        # Posição inicial dos quadrados
        self.posicao_inicial = POSICAO_INICIAL
        self.corpo_da_cobra = []
        self.criando_a_cobra()
        self.cabeca = self.corpo_da_cobra[0]

    def criando_a_cobra(self):
        # Criando a cobra
        for posicao in self.posicao_inicial:
            self.adiciona_segmento(posicao)

    def movendo(self):
        # Movimentação da cobra
        for seg_num in range(len(self.corpo_da_cobra) - 1, 0, -1):
            novo_x = self.corpo_da_cobra[seg_num - 1].xcor()
            novo_y = self.corpo_da_cobra[seg_num - 1].ycor()
            self.corpo_da_cobra[seg_num].goto(novo_x, novo_y)
        self.cabeca.forward(DISTANCIA_QUE_SE_MOVE)

    def extend(self):
        self.adiciona_segmento(self.corpo_da_cobra[-1].position())

    def adiciona_segmento(self, posicao):
        segmento = Turtle("square")
        segmento.color("white")
        segmento.penup()
        segmento.goto(posicao)

        self.corpo_da_cobra.append(segmento)

    def up(self):
        if self.cabeca.heading() != DOWN:
            self.cabeca.setheading(UP)

    def down(self):
        if self.cabeca.heading() != UP:
            self.cabeca.setheading(DOWN)

    def left(self):
        if self.cabeca.heading() != RIGHT:
            self.cabeca.setheading(LEFT)

    def right(self):
        if self.cabeca.heading() != LEFT:
            self.cabeca.setheading(RIGHT)
