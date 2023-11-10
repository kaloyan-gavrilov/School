list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
result_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        result_list.append(list1[i] + " " + list2[j])

print(result_list)
# Concatenate two lists in the following order: (permutations)
