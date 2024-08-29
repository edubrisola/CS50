import csv
from cs50 import SQL

db = SQL("sqlite:///movies.db")

titles = db.execute("SELECT * FROM movies LIMIT 30")

for i in range(30):
    print(titles[i])
