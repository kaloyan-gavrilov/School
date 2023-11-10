this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
keys_to_extract = []
result_dict = {}

while True:
    keys_to_extract.append(input("Enter a key to extract from the dict(q to quit entering): "))
    if "q" in keys_to_extract:
        break

for i in range(len(keys_to_extract)):
    if keys_to_extract[i] in this_dict:
        result_dict[keys_to_extract[i]] = this_dict[keys_to_extract[i]]

print(result_dict)

# Create a new dictionary by extracting the following keys
# from a below dictionary
# Given dictionary:
#
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# Keys to extract
# keys = ["name", "salary"]
#
# Expected output:
# (name': 'Kelly', 'salary': 8000}
