accepted_coins = [25, 10, 5]

change = 0

while True:
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        change += coin
    if change >= 50:
        break
    print("Amount Due: " + str(change))
    

print("Change Owed: " + str(change - 50))
