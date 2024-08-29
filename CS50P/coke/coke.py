amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    amount_due -= coin

    if coin != 25 and coin != 10 and coin != 5:
        amount_due += coin

if amount_due < 0:
    print(f"Change Owed: {amount_due * (-1)}")
else:
    print("Change Owed: 0")
