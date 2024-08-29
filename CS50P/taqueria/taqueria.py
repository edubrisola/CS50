PRICES = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    total = float(0)

    while True:
        try:
            name = input("Item: ").lower()

            if name == '':
                break

        except EOFError:
            break

        if name in PRICES:
            total += PRICES[name]
            print(f"Total: ${total:.2f}")

main()
