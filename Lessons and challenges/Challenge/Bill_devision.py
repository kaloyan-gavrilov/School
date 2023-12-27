def bonAppetit(bill, no_eat, pay):
    actual_pay = sum(bill) - bill[no_eat]
    actual_pay = actual_pay / 2
    if pay == actual_pay:
        return "Bon Appetit"
    else:
        return f"Brian needs to return {pay - actual_pay}"


bill = (3, 10, 2, 9)
didnt_eat = 1
pay = 7
print(bonAppetit(bill, didnt_eat, pay))

# https://www.hackerrank.com/challenges/bon-appetit/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=30-day-campaign
