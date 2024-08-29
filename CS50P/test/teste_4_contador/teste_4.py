def main():

    PHRASE = {}

    phrase = input("Phrase: ").replace(" ", "").upper()

    for char in phrase:
        if char not in PHRASE:
            PHRASE[char] = 1
        elif char in PHRASE:
            PHRASE[char] += 1

    PHRASE = dict(sorted(PHRASE.items(), key=lambda item: item[1]))

    for char in reversed(PHRASE):
        print(f"Letter: {char} || Times: {PHRASE[char]}")


if __name__ == "__main__":
    main()
