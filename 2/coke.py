amount = 50
coins = [5, 10, 25]

print(f"Amount Due: {amount}")
while amount > 0:
    coin = int(input("Insert Coin: "))
    if coin in coins:
        amount -= coin

    if amount <= 0:
        print(f"Change Owed: {-amount}")
    else:
        print(f"Amount Due: {amount}")
