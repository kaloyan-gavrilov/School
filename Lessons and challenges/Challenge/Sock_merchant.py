import random


def sockMerchant(n, arr):
    count = 1
    pair = 0
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            count += 1
    pair += count // 2
    print(pair)


n = 10
arr = []
for i in range(n):
    arr.append(random.randint(0, 10))


sockMerchant(n, arr)


# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
