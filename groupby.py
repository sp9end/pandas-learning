import pandas as pd

df = pd.read_csv("books.csv")

# ile książek napisał każdy autor
author_counts = df.groupby("author")["title"].count()
print(author_counts)

# średnia ocena per autor
avg_rating = df.groupby("author")["rating"].mean()
print(avg_rating.sort_values(ascending=False).head(10))

# kilka agregacji naraz
author_stats = df.groupby("author").agg(
    book_count=("title", "count"),
    avg_rating=("rating", "mean"),
    avg_pages=("pages", "mean")
)
print(author_stats.sort_values("book_count", ascending=False).head(10))

# dodajemy kolumnę z dekadą
df["decade"] = (df["year"] // 10) * 10

# ile książek per dekada
decade_counts = df.groupby("decade")["title"].count()
print(decade_counts)

# średnia ocena per dekada
decade_avg = df.groupby("decade")["rating"].mean()
print(decade_avg.round(2))