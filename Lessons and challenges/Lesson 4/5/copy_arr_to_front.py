import os
def copy_array_to_the_front(file_name, array):
    temp_file = "temp_file.txt"
    with open(file_name, "r") as reader:
        with open(temp_file, "w") as writer:
            for el in array:
                writer.write(str(el) + '\n')
            lines = reader.readlines()
            for line in lines:
                writer.write(line)
    os.remove(file_name)
    os.rename(temp_file, file_name)
    with open(file_name, "r") as reader:
        line = reader.readline()
        while line != "":
            print(line)
            line = reader.readline()


name = input("Enter the name of the file: ")
arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
copy_array_to_the_front(name, arr)

# Again, a function that takes a file name and an array as arguments. The function adds
# the contents of the array as rows in the file, but adds them first.
