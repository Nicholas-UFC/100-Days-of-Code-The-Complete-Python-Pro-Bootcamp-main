import time
from turtle import Screen

from bola import Bola
from jogador import Jogador
from score import Score

# Configurando a tela
tela = Screen()
tela.bgcolor("Black")
tela.setup(width=800, height=600)
tela.title("Pong")
tela.tracer(0)

# Criando os jogadores
jogador_1 = Jogador(-350, 0)
jogador_2 = Jogador(350, 0)

# Criando a bola
bola = Bola()

# Criando a pontuacao
pontos = Score()

tela.listen()
tela.onkey(jogador_1.go_up, "Up")
tela.onkey(jogador_1.go_down, "Down")
tela.onkey(jogador_2.go_up, "w")
tela.onkey(jogador_2.go_down, "s")


ligado = True
while ligado:
    tela.update()
    bola.movendo()
    time.sleep(bola.move_speed)

    # detectar colicao com o muro
    if bola.ycor() > 200 or bola.ycor() < -200:
        bola.colicao_y()

    if (
        bola.distance(jogador_1) < 50
        and bola.xcor() < -340
        or bola.distance(jogador_2) < 50
        and bola.xcor() > 340
    ):
        bola.colicao_x()

    # dectando a pontuacao
    if bola.xcor() > 380:
        bola.reset_posicao()
        pontos.ponto_jogador_2()
        pontos.update()

    if bola.xcor() < -380:
        bola.reset_posicao()
        pontos.ponto_jogador_1()
        pontos.update()

tela.exitonclick()
