# for é uma função que permite fazer uma estrutura de repetição que vai repetir X vezes, sendo X igual ao numero que está no for.
fruits = ["Apple", "Peach", "Pear"]

# Nesse exemplo, foi executado 3 vezes, pois primeiro ele pega a variavel fruit e armazena dentro dele o primeiro valor da lista fruits, depois executa 1 vez, isso repetido mais duas vezes, pois de duas vezes não existem mais valores dentro da lista fruits.
for fruit in fruits:
    print(fruit)

# Para executar uma for usando numeros em vez de lista é preciso usar a função range.
for number in range(1, 10):
    print(number)

# Como pode ser notado, começou em zero e foi até 9, pois em python a contagem começa em zero.

# Caso queira fazer com que o range pule de 2 em 2 em vez de 1 em 1, é precio colocar mais um valor em range.
for number in range(1, 10, 2):
    print(number)
