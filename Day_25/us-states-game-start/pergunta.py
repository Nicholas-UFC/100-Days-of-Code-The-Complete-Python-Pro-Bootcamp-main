import pandas as pd


def resposta(estado: str):
    dataframe = pd.read_csv(r"Day_25\us-states-game-start\50_states.csv")
    estado_cap = estado.capitalize()
    lista_de_estados = dataframe["state"].to_list()

    if estado_cap in lista_de_estados:
        for i, valor in enumerate(dataframe["state"]):
            if estado_cap == valor:
                linha = i

        for i, valor in enumerate(dataframe["x"]):
            if i == linha:
                coor_x = valor

        for i, valor in enumerate(dataframe["y"]):
            if i == linha:
                coor_y = valor

        print(f"O seu estado é {estado_cap}: x:{coor_x} e y:{coor_y}")
        return coor_x, coor_y

    elif estado_cap == "Sair":
        coor_x = -1000
        coor_y = -1000
        return coor_x, coor_y

    else:
        coor_x = 1000
        coor_y = 1000
        return coor_x, coor_y
