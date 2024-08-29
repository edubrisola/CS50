import random

def main():
    level = get_level()

    score = getOperations(level)

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue


def generate_integers(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    raise ValueError("Invalid level")


def getOperations(level):

    operations = 0
    corr_operations = 0
    wrong_answer = 0

    while operations < 10:
        x = generate_integers(level)
        y = generate_integers(level)
        corr_answer = x + y

        while True:
                try:
                    answer = input(f"{x} + {y} = ")

                    if answer.isnumeric():
                        answer = int(answer)

                        if answer == corr_answer:
                            corr_operations += 1
                            operations += 1
                            break
                        elif answer != corr_answer and wrong_answer < 2:
                            print("EEE")
                            wrong_answer += 1
                            continue
                        elif answer != corr_answer and wrong_answer == 2:
                            print(f"{x} + {y} = {corr_answer}")
                            wrong_answer = 0
                            operations += 1
                            break

                    else:
                        print("EEE")
                        wrong_answer += 1

                        if wrong_answer == 3:
                            print(f"{x} + {y} = {corr_answer}")
                            wrong_answer = 0
                            operations += 1
                            break

                        continue
                except ValueError:
                    continue

                else:
                    break

    return corr_operations


if __name__ == "__main__":
    main()
