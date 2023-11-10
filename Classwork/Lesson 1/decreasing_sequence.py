def is_decreasing(seq):

    is_decreasing = 1
    for i in range(0, int(len(seq)-1)):
        first_element = seq[i]
        second_element = seq[i+1]

        if first_element > second_element:
            continue
        else:
            is_decreasing = 0
            break
    return is_decreasing == 1


# seq = [5, 4, 3, 2, 1]
# seq = [1, 2, 3]
# seq = [100, 50, 20]
seq = [1, 1, 1]

print(is_decreasing(seq))
