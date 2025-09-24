from menu import MENU, recursos


# Função para calcular o tanto de dinheiro que a pessoa vai colocar na maquina
def pedir_moedas():
    cinco_centavos = int(input("Digite quantas moedas de 5 centavos vai colocar: "))
    print("\n")
    dez_centavos = int(input("Digite quantas moedas de 10 centavos vai colocar: "))
    print("\n")
    vinte_e_cinco_centavos = int(
        input("Digite quantas moedas de 25 centavos vai colocar: ")
    )
    print("\n")
    cinquenta_centavos = int(
        input("Digite quantas moedas de 50 centavos vai colocar: ")
    )
    print("\n")
    um_real = int(input("Digite quantas moedas de 1 real vai colocar: "))
    print("\n")
    dinheiro = (
        cinco_centavos * 5
        + dez_centavos * 10
        + vinte_e_cinco_centavos * 25
        + cinquenta_centavos * 50
        + um_real * 100
    )
    return dinheiro


# Função para fazer o café
def fazer_cafe(dinheiro, MENU, recursos, escolhido):
    # Primeiro armazenando quanto item deve ser feito
    if escolhido == 1:
        item = "espresso"
    elif escolhido == 2:
        item = "latte"
    elif escolhido == 3:
        item = "caputino"

    total = dinheiro / 100
    custo_do_cafe = MENU[item]["custo"] * 100
    # Olhando se a pessoa tem dinheiro o suficiente
    if dinheiro < custo_do_cafe:
        print("Dinheiro insuficiente!")
        print(f"Aqui seu dinheiro: R${total:.2f}")
        voltar = input("Tecle qualquer botão para voltar!!!")
        return False

    # Olhando se na maquina tem ingredientes o suficiente
    for i in recursos:
        if recursos[i] < MENU[item]["ingredientes"][i]:
            print(
                f"Não estamos com ingredientes o suficiente para fazer seu café {item} agora!"
            )
            print(f"Aqui seu dinheiro: R${total:.2f}")
            voltar = input("Tecle qualquer botão para voltar!!!")
            return False

    # Diminuindo os ingredientes da maquina
    for i in recursos:
        recursos[i] -= MENU[item]["ingredientes"][i]

    troco = (dinheiro - custo_do_cafe) / 100
    print(f"Aqui está seu café {item} e aqui está seu troco: R${troco:.2f}")
    print("\n")
    voltar = input("Tecle qualquer botão para voltar!!!")
