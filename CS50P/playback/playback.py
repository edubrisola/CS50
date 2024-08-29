phrase = input("Phrase: ")

for i in range(len(phrase)):
    if phrase[i] == ' ':
        print("...", end="")
    else:
        print(phrase[i], end="")
print("")
