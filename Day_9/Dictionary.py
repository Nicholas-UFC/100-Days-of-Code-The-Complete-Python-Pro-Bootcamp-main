# Dicionarios no Python são uma forma de armazenas dados que é possivel guarda uma informação junto de uma chave.
# Se parece com a lista, mas em vez de "[]" se usa "{}". A chave vem primeiro, depois ":" para colocar em seguida a informação a ser armazenada com base nessa chave, para separar novas informações deve ser separadas por ","
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Fuction": "A piece of code that you can easily call over and over again",
}
# É esperado que o dictionary seja de uma forma que seja facil de ler, colocando a primeira chave, depois pulando a linha e colocando a proxima informação em seguida com o proximo item do dicionario, deixando em uma linha separada a ultima chave.
# É sempre bom deixar uma virgula sobrando para que seja preciso escrever algo já que fique facil de adicionar.

# Para chamar uma informação em especifico do dicionario sera perciso escrever o nome do dicionario, depois coloca entre "[]" a chave da informação.
print(programming_dictionary["Bug"])

# Para adicionar um novo item ao dicionario, basta escrever o nome do dicionario, depois coloca em "[]" o nome da nova chave e depois coloca a informação a ser armazenada na variavel.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary["Loop"])

# Caso seja preciso apagar o dicionario basta sobre-escrever a informação com um par de "{}"
# programming_dictionary = {}
# print(programming_dictionary)

# Caso eu queira sobre-escrever uma informação de uma determinada chave, basta eu chamar o dicionario junto de sua chave e armazenar a nova informação.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Caso eu percorra um dicionario, como faço com uma lista, o valor a ser armazenado vai ser as chaves e não informação.
# Abaixo temos um exemplo e o modo para mostrar a chave e mostrar a informação daquela chave.
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
