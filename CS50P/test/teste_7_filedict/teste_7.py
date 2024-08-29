import csv

def get_dic():
    with open("teste_7.txt") as file:
        reader = csv.DictReader(file)
        reader = sorted(reader, key=lambda x:x["name"])
        return reader


def main():
    array = get_dic()
    print(array)
    return


if __name__ == "__main__":
    main()
