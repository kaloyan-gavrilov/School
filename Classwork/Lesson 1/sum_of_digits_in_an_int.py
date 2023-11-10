def sum_of_digits(n):
    n = abs(n)
    sum = 0
    while n != 0:
        sum = sum + n%10
        n = n//10

    return sum

n = int(input('Enter a number: '))
print(sum_of_digits(n))