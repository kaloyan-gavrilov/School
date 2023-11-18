def copy_n_line(name, n):
    with open(name, "a") as append:
        with open("test.txt", "r") as reader:
            lines = reader.readlines()
            for i in range(n-1, len(lines),n):
                append.write(lines[i])

    with open(name, "r") as reader:
        line = reader.readline()
        while line != "":
            print(line)
            line = reader.readline()
    return 0
file_name = input("Enter file name: ")
lines = int(input("Enter line number: "))
copy_n_line(file_name, lines)


# Write a function that takes 2 arguments - the name of a new file that will be
# created and a number "n". The function should create a new file with the corresponding name and overwrite the
# every nth line of test.txt into it.
