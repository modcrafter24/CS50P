accepted_coins = [25, 10, 5]

coin_sum = 0

while True:
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        coin_sum += coin
    if coin_sum >= 50:
        break
    print("Amount Due: " + str(50 - coin_sum))
    

print("Change Owed: " + str(coin_sum - 50))
