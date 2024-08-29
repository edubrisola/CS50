expression = input("Expression: ").lower()

x, operation, y = expression.split(" ")

x = float(x)
y = float(y)

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Error")
