import re


def print_permutation_lines(file_name):
    new_num = ""
    with open(f"{file_name}.txt", "r") as reader:
        lines = reader.readlines()
        for i in range(len(lines)):
            if len(lines) >= i + 1:
                base_set = set()
                base_set_position = i
                numbers = re.findall(r'\d+', lines[i])
                numbers = [int(num) for num in numbers]
                base_set = set(numbers)
                # print(base_set)
                temp_set = set()
                for j in range(i, len(lines)):
                    temp_set_position = j
                    numbers = re.findall(r'\d+', lines[j])
                    numbers = [int(num) for num in numbers]
                    temp_set = set(numbers)
                if base_set == temp_set:
                    if base_set_position != temp_set_position:
                        print(f'{base_set_position} -> {temp_set_position}')


name = input("Enter the file name: ")
print_permutation_lines(name)

