from turtle import Screen, Turtle
import time
from snake import Snake


# Criando a tela e configurando a tela
tela = Screen()
tela.setup(width=600, height=600)
tela.title("Jogo da Cobrinha")
tela.bgcolor("Black")
tela.tracer(0)

cobra = Snake()

# Criando os controles
tela.listen()
tela.onkey(cobra.up, "Up")
tela.onkey(cobra.down, "Down")
tela.onkey(cobra.left, "Left")
tela.onkey(cobra.right, "Right")

ligado = True
while ligado:
    tela.update()
    time.sleep(0.05)

    cobra.movendo()

tela.exitonclick()
