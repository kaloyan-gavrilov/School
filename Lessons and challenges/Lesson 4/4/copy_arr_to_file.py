import os


def copy_array_to_file(file_name, array):
    if not os.path.exists(file_name):
        file = open(file_name, "x")
        file.close()
    with open(file_name, "a") as append:
        for el in array:
            append.write(str(el) + '\n')

    with open(file_name, "r") as reader:
        line = reader.readline()
        while line != "":
            print(line)
            line = reader.readline()

    return 0


name = input("Enter the file name: ")
arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
copy_array_to_file(name, arr)

# Write a function that takes a file name and an array as arguments. The function
# creates the file if it does not exist and writes the contents of the array to individual lines in the file. If
# the file exists adds the array elements as lines in the file.
