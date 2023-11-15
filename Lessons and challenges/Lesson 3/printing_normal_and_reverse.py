list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(len(list1)):
    print(f"{list1[i]} \t {list2[-i - 1]}")
# Given a two Python list. Iterate both lists simultaneously
# such that list1 should display item in original order and list2
# in reverse order
