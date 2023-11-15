def to_digits(n):
    n = abs(n)
    arr_of_digits = []
    while n != 0:
        arr_of_digits.append(n%10)
        n = n//10
    
    return arr_of_digits

n = int(input("Enter a number:" ))
print(to_digits(n))