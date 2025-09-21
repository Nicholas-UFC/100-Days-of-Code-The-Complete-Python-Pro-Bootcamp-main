import random
from baralho import lista_de_cartas, numeros, nobres


# Função para puxar carte do baralho sem puxar carta repetida
def draw(lista_ja_tirada):
    nova_carta = random.randint(0, 51)
    while nova_carta in lista_ja_tirada:
        nova_carta = random.randint(0, 51)

    return nova_carta


# Função para contar o valor da mão
def contar(mao, carta):
    if carta in nobres:
        nova_mao = mao + 10
    elif carta == "A":
        if mao < 11:
            nova_mao = mao + 11
        else:
            nova_mao = mao + 1
    else:
        nova_mao = mao + int(carta)

    return nova_mao


# Lista das cartas já tirada e as mãos do jogador e maquina
lista_ja_tirada = []
cartas_do_jogador_1 = []
valor_do_jogador_1 = 0
cartas_da_maquina = []
valor_da_maquina = 0

# Primeira mão do jogador
carta_1 = draw(lista_ja_tirada)
lista_ja_tirada.append(carta_1)
cartas_do_jogador_1.append(lista_de_cartas[carta_1])
valor_do_jogador_1 = contar(valor_do_jogador_1, lista_de_cartas[carta_1])

carta_2 = draw(lista_ja_tirada)
lista_ja_tirada.append(carta_2)
cartas_do_jogador_1.append(lista_de_cartas[carta_2])
valor_do_jogador_1 = contar(valor_do_jogador_1, lista_de_cartas[carta_2])

# Primeria mão da maquina
carta_1 = draw(lista_ja_tirada)
lista_ja_tirada.append(carta_1)
cartas_da_maquina.append(lista_de_cartas[carta_1])
valor_da_maquina = contar(valor_da_maquina, lista_de_cartas[carta_1])

carta_2 = draw(lista_ja_tirada)
lista_ja_tirada.append(carta_2)
cartas_da_maquina.append(lista_de_cartas[carta_2])
valor_da_maquina = contar(valor_da_maquina, lista_de_cartas[carta_2])

print(f"Sua primeira mão: {cartas_do_jogador_1} e valor dela {valor_do_jogador_1}")

# Pergunta pro jogador se ele quer puxar mais cartas!
acabou_o_jogo = False
nova_carta = True
while nova_carta:
    nova_carta = input("Deseja tirar uma nova carta(Y/N): ")
    nova_carta = nova_carta.upper()
    if nova_carta == "Y":
        carta_tirada = draw(lista_ja_tirada)
        lista_ja_tirada.append(carta_tirada)
        cartas_do_jogador_1.append(lista_de_cartas[carta_tirada])
        valor_do_jogador_1 = contar(valor_do_jogador_1, lista_de_cartas[carta_tirada])
        print(f"Sua mão é: {cartas_do_jogador_1}")
        print(f"Seu valor é: {valor_do_jogador_1}")

        # Olhando se já perdeu
        if valor_do_jogador_1 > 21:
            nova_carta = False
            acabou_o_jogo = True
            print(f"Sua mão tem valor {valor_do_jogador_1} e a mão da maquina tem valor {valor_da_maquina}, você perdeu!")
        elif valor_do_jogador_1 == 21:
            print(f"Sua mão tem valor {valor_do_jogador_1} e a mão da maquina tem valor {valor_da_maquina}, você venceu!")
            nova_carta = False
            acabou_o_jogo = True
        else:
            nova_carta = True

    elif nova_carta == "N":
        nova_carta = False


# A maquina puxando cartas
nova_carta = True
while nova_carta and not acabou_o_jogo:
    if valor_da_maquina > valor_do_jogador_1 and valor_da_maquina < 21:
        nova_carta = False
        print(
            f"Sua mão tem valor {valor_do_jogador_1} e a mão da maquina tem valor {valor_da_maquina}, você perdeu!"
        )
    else:
        carta_tirada = draw(lista_ja_tirada)
        lista_ja_tirada.append(carta_tirada)
        cartas_da_maquina.append(lista_de_cartas[carta_tirada])
        valor_da_maquina = contar(valor_da_maquina, lista_de_cartas[carta_tirada])

    if valor_da_maquina == 21:
        print(f"Sua mão tem valor {valor_do_jogador_1} e a mão da maquina tem valor {valor_da_maquina}, você perdeu!")
        nova_carta = False

    if valor_da_maquina > 21:
        print(f"Sua mão tem valor {valor_do_jogador_1} e a mão da maquina tem valor {valor_da_maquina}, você venceu!")
        nova_carta = False
