def to_number(digits):
    digits.reverse()
    i = 1
    number = 0
    for element in digits:
        number += element*i
        i = i*10
    return number


digits = [1, 2, 3]


print(to_number(digits))
