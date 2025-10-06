import csv


with open(r"Day_25\weather_data.csv") as data:
    dataframe = csv.reader(data)
    temperatura = []
    for linha in data:
        celulas = linha.split(",")
        temperatura.append(celulas[1])
    temperatura.pop(0)
    print(temperatura)