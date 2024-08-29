def main():
    string = input("Input: ")
    string = shorten(string)

    print(string)

def shorten(string):
    new_string = ""

    for char in string:
        if char.lower() not in 'aeiou':
            new_string += char

    return new_string


if __name__ == "__main__":
    main()
