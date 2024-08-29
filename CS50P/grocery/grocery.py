NAMES = {}

def main():
    while True:
        try:
            name = input()

            if name == '':
                break
            elif name in NAMES:
                NAMES[name] += 1
            elif name not in NAMES:
                NAMES[name] = 1

        except EOFError:
            break

    for words in sorted(NAMES.keys()):
        if words != '':
            print(f"{NAMES[words]} {words.upper()}")
main()
