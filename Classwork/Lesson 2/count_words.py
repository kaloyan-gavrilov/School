def count_words(arr):
    word_count = {}
    for element in arr:
        word_count[element] = arr.count(element)
    return word_count



print(count_words(["apple", "banana", "apple", "pineapple"]))
print(count_words(["python", "python", "python", "ruby"]))


# Given a list of strings, implement a function, called count_words(arr) which returns a
# dictionary of the following kind:
# { "word" : count }
# Where count is the count of occurrences of the word in the list arr.