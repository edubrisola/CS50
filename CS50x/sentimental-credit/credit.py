def validCredit(number, z):

    i = z - 1
    a = 0
    sum = 0

    if (z % 2 == 0):
        while a < i:
            digit = int(number[a]) * 2
            if digit > 9:
                digit = digit - 9
            sum = sum + digit
            sum = sum + int(number[a + 1])
            a = a + 2

    else:
        sum = int(number[0])
        while (a + 1) < i:
            digit = int(number[a + 1]) * 2
            if digit > 9:
                digit = digit - 9
            sum = sum + digit
            sum = sum + int(number[a + 2])
            a = a + 2

    return sum

def creditFlag(number, z):

    fd = 10 * int(number[0]) + int(number[1])

    if ((fd == 34) or (fd == 37)) and (z == 15):
        print("AMEX\n")
    elif ((fd == 51) or (fd == 52) or (fd == 53) or (fd == 54) or (fd == 55)) and (z == 16):
        print("MASTERCARD\n")
    elif (int(number[0]) == 4) and ((z == 13) or (z == 16)):
        print("VISA\n")
    else:
        print("INVALID\n")


def main():
    number = input("Number: ")
    z = len(number)
    x = validCredit(number, z)

    if (x % 10) == 0:
        creditFlag(number, z)
    else:
        print("INVALID\n")


if __name__ == "__main__":
    main()

