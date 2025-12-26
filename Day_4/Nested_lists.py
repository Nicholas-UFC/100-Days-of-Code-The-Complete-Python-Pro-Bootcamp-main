# É possivel armazenar uma lista dentro de uma lista, isso é chamado de Nested Lists.
dirty_dozen = [
    "Strawberries",
    "Spinach",
    "Kale",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
    "Tomatoes",
    "Celery",
    "Potatoes",
]

# Vamos dividir dirty_dozen em vegetais e frutas.
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Com isso armazenamos na primeira posição uma lista e uma segunda lista na segunda posição.
dirty_dozen_nested_list = [fruits, vegetables]
print(dirty_dozen_nested_list)
