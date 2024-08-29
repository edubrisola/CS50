import re


def main():
    print(count(input("Text: ").strip()))


def count(string):
    matches = re.findall(r'\bum\b', string, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
