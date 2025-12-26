from turtle import Screen, Turtle

# Criar objetos
joao = Turtle()
tela = Screen()


# Funções de se mover
def mover_pra_frente():
    joao.forward(10)


def mover_pra_tras():
    joao.backward(10)


def sentido_horario():
    joao.right(15)


def sentido_anti_horario():
    joao.left(15)


def limpar():
    joao.clear()
    joao.penup()
    joao.home()
    joao.pendown()


# Função das teclas
def movimentacao():
    tela.onkey(mover_pra_frente, "w")
    tela.onkey(mover_pra_tras, "s")
    tela.onkey(sentido_horario, "d")
    tela.onkey(sentido_anti_horario, "a")
    tela.onkey(limpar, "space")


# Começar o app
if __name__ == "__main__":
    tela.listen()
    movimentacao()
    tela.exitonclick()
