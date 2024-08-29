string = input("camelCase: ")

for i in range(len(string)):
    if string[i].isupper():
        print(f"_{string[i].lower()}", end="")
    else:
        print(f"{string[i].lower()}", end="")
print()
