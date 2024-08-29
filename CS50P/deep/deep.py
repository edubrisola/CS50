def main():
    enter = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

    if enter.lower() == "forty two" or enter.lower() == "forty-two":
        print("Yes")
        return

    try:
        enter_int = int(enter)
        if enter_int == 42:
            print("Yes")
            return
    except ValueError:
        pass

    print("No")

if __name__ == "__main__":
    main()
