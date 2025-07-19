#List é um de estrutura de dados que existe no python que serve para armazenar um vetor de valores.
#Abaixo nos temos um vetor que armazena todos os estados dos EUA, é utilizado [] para definir list e os diversos valores são dividos por uma virgula.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Se eu printar o vetor inteiro vai ser exibido toda a lista.
print(states_of_america)

#Se eu quiser printar apenas o primeiro valor da lista, basta eu escrever o nome do vetor e a posição que está indexada a ela. Sendo que a contagem de uma lista sempre começa com 0.
print(states_of_america[0])

#É possivel colocar valores negativos, caso isso ocorra, então ele vai devolver valores do final pro inicio, sendo que a posição 0 sempre vai ser 0.
print(states_of_america[-1])

#Também posso armazenar valores dentro da lista sem alterar ela toda.
states_of_america[1] = "Pencilvania"
print(states_of_america)

#Existe diversas funções que pode ser aplicada em uma lista, uma delas é a .extend que permite adicionar novos itens a lista, colocando os novos valores no final da lista.
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)