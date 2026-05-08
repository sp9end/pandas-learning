import pandas as pd

# wczytanie pliku CSV
df = pd.read_csv("books.csv")

# pierwsze 5 wierszy
print(df.head())

# ostatnie 5 wierszy
print(df.tail())

# podstawowe informacje o DataFrame
print(df.info())

# podstawowe statystyki
print(df.describe())