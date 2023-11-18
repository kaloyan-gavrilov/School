import os


def copy_reverse(file_name):
    with open(file_name, "w") as writer:
        with open("test.txt", "r") as reader:
            lines = reader.readlines()
            for line in reversed(lines):
                writer.write(line)

    os.remove("test.txt")

    with open(file_name, "r") as reader:
        line = reader.readline()
        while line != "":
            print(line)
            line = reader.readline()
    return 0


name = input("Enter file name: ")
copy_reverse(name)

# Write a function that overwrites the contents of test.txt line by line in a new file, but
# in reverse order. Bonus: delete the first file. (It's a good idea to make a copy of test.txt to
# you don't have to retype it every time)
