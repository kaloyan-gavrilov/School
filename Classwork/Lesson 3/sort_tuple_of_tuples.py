this_tuple = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
result_tuple = tuple(sorted(this_tuple, key=lambda x: x[1]))
print(result_tuple)
# Sort a tuple of tuples by 2nd item
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# Expected output:
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))
