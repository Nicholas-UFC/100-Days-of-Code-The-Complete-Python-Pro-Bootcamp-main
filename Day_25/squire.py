import pandas as pd

esquilos = pd.read_csv(
    r"Day_25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251006.csv"
)

contagem_final_df = esquilos["Primary Fur Color"].value_counts().reset_index()
contagem_final_df.columns = ["Cor do Pelo", "Contagem"]
print(contagem_final_df)
