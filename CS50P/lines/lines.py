import sys

def main():

    args = len(sys.argv)

    if args < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif args > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].count(".py") != 1:
        print("Not a Python file")
        sys.exit(1)
    else:
        lines_n = openFile(sys.argv[1])
        print(lines_n)


def openFile(filename):

    lines_n = 0
    with open(filename, "r") as file:

        for lines in file:
            if lines.strip() and not lines.strip().startswith("#"):
                lines_n += 1
    return lines_n

if __name__ == "__main__":
    main()
