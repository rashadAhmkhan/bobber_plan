prices = []

def stockPrice(l):
    lowest_price = l[0]
    highest_profit = 0

    for i in l:
        profit = i - lowest_price

        if profit > highest_profit:
            highest_profit = profit

        if i < lowest_price:
            lowest_price = i

    return highest_profit

print(stockPrice(prices))