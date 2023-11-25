from colorama import Fore


def unique_word(source_file, export_file):
    words = []
    words_count = {}
    choice = False
    if input("Do you want to print the words in ascending order?(Yes/No) ") == "Yes":
        choice = True
    with open(f"{source_file}.txt", "r") as reader:
        lines = reader.readlines()
        new_word = ""
        for line in lines:
            for i in line:
                if i == " " or i == '\n' or i == "." or i == ",":
                    words.append(new_word)
                    new_word = ""
                    continue

                new_word = new_word + i
    for word in words:
        if word in words_count:
            continue
        else:
            words_count[word] = words.count(word)
    del words_count[""]

    with open(f"{export_file}.txt", "w") as writer:
        for key, value in words_count.items():
            writer.write(f"{key} -> {value} \n")

    if choice is True:
        with open(f"{export_file}.txt", "a") as writer:
            writer.write("\n\n Words in ascending order: \n\n")
            in_ascending = {key: val for key, val in sorted(words_count.items(), key=lambda ele: ele[1], reverse=True)}
            for key, value in in_ascending.items():
                writer.write(f"{key} -> {value} \n")


file_name = input(Fore.LIGHTWHITE_EX + "Enter the file name: ")

while True:
    new_file = input(Fore.LIGHTWHITE_EX + "Enter new file name: ")
    if new_file == file_name:
        print(Fore.RED + "Names are the same")
    else:
        break

unique_word(file_name, new_file)
