import os
def rename_file(file_name, new_name):
    os.rename(file_name, new_name)

f_name = input("Enter the file you want to rename: ")
n_name = input("Enter the new name of the file: ")
rename_file(f_name, n_name)

# Rename file (via code)
