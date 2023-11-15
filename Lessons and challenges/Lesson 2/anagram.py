def is_anagram(fst_word, snd_word):
    if len(fst_word) != len(snd_word):
        return False
    fst_word = fst_word.lower()
    snd_word = snd_word.lower()
    chars_of_fst_word = {}
    chars_of_snd_word = {}
    for i in range(0, len(fst_word)):
        chars_of_fst_word[fst_word[i]] = i
        chars_of_snd_word[snd_word[i]] = i
    return chars_of_fst_word.keys() == chars_of_snd_word.keys()


first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")

print(is_anagram(first_word, second_word))

# For anagrams, check here - https://en.wikipedia.org/wiki/Anagram
# For example, listen and silent are anagrams.
# Implement a function is_anagram(a, b), which returns True, if the string a is an
# anagram of b.
# Consider lowering the case of the two words since the case does not matter. SILENT
# and listen are also anagrams.