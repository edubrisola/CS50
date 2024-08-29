import sys
import csv

def main():

    NAMES = []

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]
    fileout = sys.argv[2]

    if not filename.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    NAMES = getDict(filename, NAMES)
    output(NAMES, fileout)
    print(NAMES)

    return


def getDict(filename, NAMES):
    with open(filename, "r") as file:

        dic = csv.DictReader(file)
        for line in dic:
            last, first = line["name"].split(",")
            names = {}
            if first not in names:
                names['first'] = first.strip()
                names['last'] = last.strip()
                names['house'] = line["house"]

                NAMES.append(names)
    NAMES = sorted(NAMES, key=lambda x: x['first'])
    return NAMES


def output(NAMES, filename):
    with open(filename, "w") as file:
        file.write("first,last,house\n")

        for names in NAMES:
            file.write(f"{names['first']},{names['last']},{names['house']}\n")


if __name__ == "__main__":
    main()
