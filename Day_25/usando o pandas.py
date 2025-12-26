import pandas as pd

dataframe = pd.read_csv(r"Day_25\weather_data.csv")

# print(dataframe["temp"])

# data_dict = dataframe.to_dict()
# print(data_dict)

# temp_list = dataframe["temp"].to_list()
# print(temp_list)

# print(dataframe["temp"].mean())

# print(dataframe["temp"].max())

lista = [i for i, valor in enumerate(dataframe["day"] == "Monday") if valor]

print(dataframe.iloc[lista])
