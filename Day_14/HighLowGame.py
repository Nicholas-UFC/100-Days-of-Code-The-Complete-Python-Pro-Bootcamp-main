import random

from lista import lista_de_pessoas


# Declara as variaveis
pontuacao = 0
jogo = True
repetido = True
ja_foi = []
pessoa_1 = random.randint(0, (len(lista_de_pessoas) - 1))
pessoa_2 = random.randint(0, (len(lista_de_pessoas) - 1))

# Olha se não criou duas pessoas iguais
while repetido:
    if pessoa_1 == pessoa_2:
        pessoa_2 = random.randint(0, (len(lista_de_pessoas) - 1))
        repetido = True
    else:
        repetido = False

ja_foi.append(pessoa_1)
ja_foi.append(pessoa_2)


# Olha se não está criando uma pessoas que já foi
def ja_foi_ou_nao(pessoa_2):
    loop = True
    while loop:
        if pessoa_2 in ja_foi:
            pessoa_2 = random.randint(0, (len(lista_de_pessoas) - 1))
            loop = True
        else:
            loop = False
    ja_foi.append(pessoa_2)

    return pessoa_2


# Começa o loop do jogo
print("Vamos jogar HighLowGame!!!")
while jogo:
    print("Quem tem mais seguidores no instagram???")
    print(
        f"\n{lista_de_pessoas[pessoa_1]['nome']}, que é {lista_de_pessoas[pessoa_1]['descricao_rapida']}, é de {lista_de_pessoas[pessoa_1]['pais_origem']}"
    )
    print(
        f"\n{lista_de_pessoas[pessoa_2]['nome']}, que é {lista_de_pessoas[pessoa_2]['descricao_rapida']}, é de {lista_de_pessoas[pessoa_2]['pais_origem']}"
    )
    chute = input("\n1 ou 2:")
    chute = int(chute)

    if (
        lista_de_pessoas[pessoa_1]["seguidores_instagram"]
        > lista_de_pessoas[pessoa_2]["seguidores_instagram"]
    ):
        pessoa_2 = ja_foi_ou_nao(pessoa_2)
        valor_do_maior = 1
    else:
        pessoa_1 = pessoa_2
        pessoa_2 = ja_foi_ou_nao(pessoa_1)
        valor_do_maior = 2

    if chute == valor_do_maior:
        pontuacao += 1
    else:
        print(f"Você errou, sua pontuação foi de {pontuacao}")
        jogo = False
