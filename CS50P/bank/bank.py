string = (input("Greeting: ").lower()).strip(" ")

if string[0:5] == "hello":
    print("$0")
elif string[0] == "h":
    print("$20")
else:
    print("$100")
