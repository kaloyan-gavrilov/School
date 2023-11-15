this_dict = {
    "a": 10,
    "b": 45,
    "c": 39,
    "d": 11,
    "e": 8
}
keys = list(this_dict.keys())
values = list(this_dict.values())
min_value = values[0]
for value in values:
    if value < min_value:
        min_value = value

key_position = values.index(min_value)
print(keys[key_position])

# Get the key of a minimum value from a dictionary
# sampleDict = {
#     "Physics": 82,
#     "Math": 65,
#     "history": 75
# }
# Expected output:
# Math
