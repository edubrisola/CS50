def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    letters_num = 0
    numbers_num = 0
    first_number = -1

    for char in plate:
        char = char.lower()
        if char.isalpha():
            letters_num += 1
            if numbers_num != 0:
                return False
        if not char.isalpha() and not char.isnumeric():
            return False

        elif char.isnumeric() and letters_num < 2:
            return False

        elif char.isnumeric() and first_number == -1:
            numbers_num += 1
            first_number = int(char)

        elif char.isnumeric() and first_number != -1:
            numbers_num += 1

    if first_number == 0:
        return False
    elif (letters_num + numbers_num) > 6 or letters_num < 2:
        return False
    else:
        return True



if __name__ == "__main__":
    main()
