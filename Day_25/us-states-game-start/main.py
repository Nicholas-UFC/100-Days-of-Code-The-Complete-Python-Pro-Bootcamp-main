import time
import turtle

from marca import Marca
from pergunta import resposta

imagem = r"Day_25\us-states-game-start\blank_states_img.gif"
tela = turtle.Screen()
tela.title("US States Game")
tela.addshape(imagem)
turtle.shape(imagem)

ligado = True
while ligado:
    pergunta_estado = str(
        tela.textinput(
            title="Adivinhe um estado",
            prompt="Qual o nome do estado? (digite sair para sair)",
        )
    )
    x, y = resposta(pergunta_estado)

    if x != 1000 and y != 1000 and x != -1000 and y != -1000:
        marcador = Marca(pergunta_estado, x, y)

    elif x == -1000 and y == -1000:
        ligado = False
    else:
        marcador = Marca("", 0, 0)
        marcador.noexiste()
        time.sleep(1)

tela.mainloop()
