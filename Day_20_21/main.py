import time
from turtle import Screen, Turtle

from food import Comida
from score import Score
from snake import Snake

# Criando a tela e configurando a tela
tela = Screen()
tela.setup(width=600, height=600)
tela.title("Jogo da Cobrinha")
tela.bgcolor("Black")
tela.tracer(0)

cobra = Snake()
comida = Comida()
pontuacao = Score()

# Criando os controles
tela.listen()
tela.onkey(cobra.up, "Up")
tela.onkey(cobra.down, "Down")
tela.onkey(cobra.left, "Left")
tela.onkey(cobra.right, "Right")

ligado = True
while ligado:
    tela.update()
    time.sleep(0.1)

    cobra.movendo()

    # Colicao com a comida
    if cobra.cabeca.distance(comida) < 15:
        pontuacao.aumentar_score()
        comida.recarregar()
        cobra.extend()

    # Detectar se bateu na parede
    if cobra.cabeca.xcor() > 280 or cobra.cabeca.xcor() < -280 or cobra.cabeca.ycor() >  280 or cobra.cabeca.ycor() < -280:
        ligado = False
        pontuacao.game_over()

    # Detectar se bateu no rabo
    for segmento in cobra.corpo_da_cobra[1:]:
        if cobra.cabeca.distance(segmento) < 10:
            ligado = False
            pontuacao.game_over()

tela.exitonclick()
