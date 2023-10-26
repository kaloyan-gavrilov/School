def sum_of_numbers(str):
    sum = 0
    temp = ""

    for i in str:
        if i.isnumeric():
            temp += i
        elif temp:
            sum += int(temp)
            temp = ""
    if temp:
        sum += int(temp)

    return sum


a = input("Enter: ")
result = sum_of_numbers(a)
print(result)

# You are given a string, where there can be numbers. Return the sum of all numbers
# in that string (not digits, numbers)
