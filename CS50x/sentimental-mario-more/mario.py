from cs50 import get_int

height = 0

while height < 1 or height > 8:
    height = get_int("Height: ")

# Loop to print each row
for i in range(1, height + 1):
    # Print leading spaces
    for j in range(height - i):
        print(" ", end="")

    # Print first set of hashes
    for j in range(i):
        print("#", end="")

    # Print gap
    print("  ", end="")

    # Print second set of hashes
    for j in range(i):
        print("#", end="")

    # Move to the next line
    print()
