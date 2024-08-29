import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <filename.csv>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader]

            table = tabulate(data, headers=headers, tablefmt="grid")
            print(table)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
