def main():
    while True:
        fraction = input("Fraction: ").strip()

        try:
            if fraction.count("/") != 1:
                continue

            number_1, number_2 = fraction.split("/")

            if number_1.count(".") != 0 or number_2.count("."):
                continue

            elif number_1.isalpha() or number_2.isalpha():
                continue

            elif int(number_1) > int(number_2):
                continue

        except ValueError:
            pass

        new_number = round((float(number_1) / float(number_2) * 100))

        if number_1 == 0 or new_number < 10:
            print("E")
            return

        elif number_1 == number_2 or new_number > 90:
            print("F")
            return

        else:
            print(f"{new_number}%")
            return

main()
