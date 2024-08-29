def main():
    string = input("Greeting: ")
    money = value(string)
    print(f"${money}")


def value(string):

    string = string.lower()

    if string[0:5] == "hello":
        return 0
    elif string[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
