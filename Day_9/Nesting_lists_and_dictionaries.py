#Nesting lista ou nesting dicionarios são listas que dentro delas tem novas listas ou dicionarios que dentro do dicionarios tem lista e ou dicionarios.

#Abaixo podemos observar que dentro dele tem uma lista.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
}

#Para chamar uma informação em uma nesting lista ou nesting dicionarios, deve ser "[]" igual ao numero de informação dentro de cada parte. Nesse caso, o primeiro é para entrar na primeira pasta e o segundo para entrar na segunda pasta.
print(travel_log["France"][1])

#Nesse exemplo para acessar o D é precio pecorrer até a posição 2 da primeira lista e depois percorrer até a primeira posição.
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12,
    },
    "Germany": {
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total_visits": 5,
    }
}

print(travel_log["France"]["Cities_visited"][2])
print(travel_log["Germany"]["Total_visits"])