with open("test.txt", "r") as reader:
    copy_file = open("copy_file.txt", "w")
    copy_file.write(reader.read())
    copy_file.close()

with open("copy_file.txt", "r") as reader:
    line = reader.read()
    while line != "":
        print(line, end=" ")
        line = reader.read()
# Create another file in the same folder and overwrite the contents of test.txt in it.
