# Projeto que entrega uma sugestão de senha composto por letras, numeros e simbolos.
# Importa biblioteca usada
import random

# Lista de letras, numeros e simbolos.
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Pergunta e armazena o numero de letras, numeros e simbolos.
print("Bem vindo ao gerador de senhas aleatorios")

num_letters = int(input("Quantas letras vai ter sua senha? "))
num_numbers = int(input("Quantos numeros vai ter sua senha? "))
num_symbols = int(input("Quantos simbolos vai ter sua senha? "))

# Armazena o tamanho da senha.
Tamanho_da_Senha = num_letters + num_numbers + num_symbols

# Cria a variavel senha sendo uma string vazia
senha = ""


# Eazy Level - Order not randomised:
# Cria uma estrutura de repetição igual ao numero de letras, numeros e simbolos escolhidos mais 1.
# Gera um numero aleatorio inteiro sendo o range igual ao numero de possibilidades da minha lista já definida.
# O numero gerado é a posição da letra/numer/simbolo escolhido.
for letter in range(1, num_letters + 1):
    Letra = random.randint(0, 25)
    senha = senha + letters[Letra]

for number in range(1, num_numbers + 1):
    Numero = random.randint(0, 9)
    senha = senha + str(numbers[Numero])

for symbol in range(1, num_symbols + 1):
    Simbolos = random.randint(0, 8)
    senha = senha + str(symbols[Simbolos])

print(f"Sua senha recomendada é: {senha}")

# Hard Level - Order of characters randomised:
# Cria a variavel senha sendo uma lista vazia
senha_list = []

# Repete a mesma estrutura de repetição de antes, mas agora sendo uma lista eles vão ser colocado na ultima posição da lista.
for letter in range(1, num_letters + 1):
    Letra = random.randint(0, 25)
    senha_list += letters[Letra]

for number in range(1, num_numbers + 1):
    Numero = random.randint(0, 9)
    senha_list += str(numbers[Numero])

for symbol in range(1, num_symbols + 1):
    Simbolos = random.randint(0, 8)
    senha_list += str(symbols[Simbolos])

# Usando a função random.shuffle() posso embaralhar os valores dentro da lista senha_list.
random.shuffle(senha_list)

# Agora vou transformar a senha_list de lista para uma string
char = ""
for i in senha_list:
    char += str(i)

print(f"Sua senha recomendada é: {char}")
