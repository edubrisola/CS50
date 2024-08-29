number = int(input("Height: "))

for height in range(number):
    height += 1
    for space1 in range(number - height):
        print(" ", end="")

    for bar1 in range(height):
        print("#", end="")

    print(" ", end="")

    for bar2 in range(height):
        print("#", end="")

    print()

