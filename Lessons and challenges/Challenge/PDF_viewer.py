import string


def designerPdfViewer(hight_alphabet, word):
    alphabet = list(string.ascii_lowercase)
    hight = 0
    for letter in word:
        if hight_alphabet[alphabet.index(letter)] > hight:
            hight = hight_alphabet[alphabet.index(letter)]
    area = hight * len(word)
    print(area)


h = (1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
word = "abc"
designerPdfViewer(h, word)

# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
