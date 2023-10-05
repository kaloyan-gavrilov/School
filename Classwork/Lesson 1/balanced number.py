def is_number_balanced(n):
    right_sum = 0
    left_sum = 0

    if int(n) > 10 and int(len(n)) % 2 == 0:
        n.replace(str(int(len(n))//2), "")
    for i in range(0, int(len(n)/2)):

        left_sum += int(n[i])
        right_sum += int(n[len(n)-1-i])
    print(f"{right_sum}, {left_sum}")
    return right_sum == left_sum


n = input("Enter number: ")
print(is_number_balanced(n))
