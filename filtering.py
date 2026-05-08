import pandas as pd

df = pd.read_csv("books.csv")

pd.set_option("display.max_columns", None)

# Selekcja kolumn
# jedna kolumna
print(df["title"])

# kilka kolumn
print(df[["title", "author", "rating"]])

# Filtrowanie wierszy
# książki z oceną 10
best = df[df["rating"] == 10]
print(best)

# książki z więcej niż 500 stronami
long_books = df[df["pages"] > 500]
print(long_books)

# książki wydane po 2000 roku Z oceną >= 9
recent_top = df[(df["year"] > 2000) & (df["rating"] >= 9)]
print(recent_top)

# książki wydane przed 1900 LUB z oceną 10
classics_or_best = df[(df["year"] < 1900) | (df["rating"] == 10)]
print(classics_or_best)

# sortowanie
# sortowanie po ocenie malejąco
print(df.sort_values("rating", ascending=False).head(10))

# sortowanie po roku rosnąco
print(df.sort_values("year").head(10))

# sortowanie po kilku kolumnach
print(df.sort_values(["rating", "pages"], ascending=[False, True]).head(10))