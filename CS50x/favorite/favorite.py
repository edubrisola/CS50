import csv

from collections import Counter

with open("dictionary.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        favorite = row["Language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

    for favorite in counts.most_common():
        print(f"{favorite}")


