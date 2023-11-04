def get_money_spent(keyboards, drives, budget):
    max_price = 0
    afford_list = []
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= budget:
                afford_list.append(keyboard + drive)
    for price in afford_list:
        if price > max_price:
            max_price = price
    if not afford_list:
        return -1
    else:
        return max_price


k = [40, 50, 60]
d = [5, 8, 12]
b = 60
print(get_money_spent(k, d, b))

# https://www.hackerrank.com/challenges/electronics-shop/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
