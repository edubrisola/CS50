import random

def main():
    while True:
        try:
            level = input("Level: ")

            if level.isalpha():
                continue
            elif level.isnumeric():
                level = int(level)

                if level > 0:
                    break
                else:
                    continue
            else:
                continue
        except ValueError:
            continue
    number = generateNumber(level)

    while True:
        try:
            trial = input("Guess: ")

            if trial.isalpha():
                continue
            elif trial.isnumeric():
                trial = int(trial)
                if trial > number:
                    print("Too large!")
                    continue
                elif trial < number:
                    print("Too small!")
                    continue
                else:
                    print("Just right!")
                    break
        except ValueError:
            continue
    return

def generateNumber(level):
    return random.randint(1, level)


if __name__ == "__main__":
    main()
