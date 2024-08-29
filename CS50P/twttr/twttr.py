string = input("Input: ")
new_string = ""

for char in string:
    if char.lower() not in 'aeiou':
        new_string += char
print(f"Output: {new_string}")
