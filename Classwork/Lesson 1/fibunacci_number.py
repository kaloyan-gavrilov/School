def fib_number(n):
    n1 = 0
    n2 = 1
    count = 0
    while count != n:
        print(n2)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1


n = int(input("Enter a number: "))
fib_number(n)
