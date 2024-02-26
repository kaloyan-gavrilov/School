def camel_case(string):
    count = 0
    for letter in string:
        if letter.isupper():
            count = count + 1

    return count + 1


string = "thisIsASentence"

print(camel_case(string))

# https://www.hackerrank.com/challenges/camelcase/problem
