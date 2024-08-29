def main():
    CANDIDATES = {}
    getInput(CANDIDATES)


def getInput(CANDIDATES):
    print()
    
    while True:
        try:
            print("1. Add Candidate\n2. Results\n3. Clear\n")
            option = input("Option: ").strip()

            if option.isnumeric():
                option = int(option)

                if option == 1:
                    addVotes()
                    continue
                elif option == 2:
                    if getVotes(CANDIDATES):
                        CANDIDATES = voteResults(CANDIDATES)
                        continue
                    else:
                        print("\nInsert One Candidate!\n")
                elif option == 3:
                    clean(CANDIDATES)
                    CANDIDATES = {}
                    continue
                else:
                    print("\nInvalid Option!\n")
                    continue

            elif option.isalpha():
                option = option.lower()

                if option == "add" or option == "add candidate":
                    addVotes()
                    continue
                elif option == "results":
                    if getVotes(CANDIDATES):
                        CANDIDATES = voteResults(CANDIDATES)
                        continue
                    else:
                        print("\nInsert One Candidate!\n")
                elif option == "clear":
                    clean(CANDIDATES)
                    CANDIDATES = {}
                    continue
                else:
                    print("\nInvalid Option!\n")
                    continue

            elif option == "":
                break

            else:
                print("\nInvalid Option!\n")
                continue

        except ValueError:
            pass
    return


def getVotes(CANDIDATES):
    with open("teste_5.txt", "r") as file:

        for line in file:
            name = line.strip()

            if name in CANDIDATES:
                CANDIDATES[name] += 1
            elif name not in CANDIDATES:
                CANDIDATES[name] = 1
    return CANDIDATES


def addVotes():
    print()

    while True:
        try:
            name = input("Candidate Name: ")

            if name.isnumeric():
                print("Ivalid Name!")
                continue
            elif name.isalpha():
                name = name.title()
            else:
                print("Ivalid Name!")
                continue

            while True:
                try:
                    number = input("Number Of Votes: ")

                    if number.isalpha():
                        print("Invalid Number!")
                        continue
                    elif number.isnumeric():
                        number = int(number)
                        break
                    else:
                        print("Invalid Number!")
                        continue

                except ValueError:
                    pass
            break
        except ValueError:
            pass

    with open("teste_5.txt", "a+") as file:

        for _ in range(number):
            file.write(f"{name}\n")
    print()


def voteResults(CANDIDATES):
    print()

    CANDIDATES = (dict(sorted(CANDIDATES.items(), key=lambda item: item[1])))
    votes_total = 0
    votes_index = 0
    winner = ""

    for candidate in CANDIDATES:
        votes_total += CANDIDATES[candidate]

        if CANDIDATES[candidate] > votes_index:
            votes_index = CANDIDATES[candidate]
            winner = candidate

    percentage = (float(votes_index)/float(votes_total)) * 100
    percentage = round(percentage, 2)

    print(f"The Winner Is {winner} With {votes_index} Votes Out Of {votes_total} Votes\n")
    print(f"Percentage Of Winning Votes: {percentage:.2f}%\n")

    for candidate in CANDIDATES:
        new_percentage = (float(CANDIDATES[candidate])/float(votes_total)) * 100
        print(f"{candidate} Votes: {CANDIDATES[candidate]} With {new_percentage:.2f}%")
    print()

    CANDIDATES = {}
    return CANDIDATES


def clean(CANDIDATES):
    with open("teste_5.txt", "w") as file:
        file.write("")

    print()


if __name__ == "__main__":
    main()
