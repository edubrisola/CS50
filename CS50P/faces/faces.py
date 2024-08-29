phrase = input("Phrase: ")

i = 0
while i < len(phrase):
    if phrase[i] == ":" and phrase[i + 1] == ")":
        print("🙂", end="")
        i = i + 2
    elif phrase[i] == ":" and phrase[i + 1] == "(":
        print("🙁", end="")
        i = i + 2
    else:
        print(phrase[i], end="")
        i += 1
print("")
