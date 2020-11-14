"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Enter a string: ') + ' '

word_counter = 0
longest_word = ''
word = ''

for i in string:
    if i.isalpha():
        word += i
    else:
        if word and len(longest_word) < len(word):
            word_counter += 1
            longest_word = word
        word = ''

print(word_counter, longest_word, len(longest_word))


# Решение с использованием библиотеки re и функции max

import re

string = input('Enter a string: ')

words = re.findall(r'[a-zA-Z]+', string)
longest_word = max(words, key=len)

print(len(words), longest_word, len(longest_word))
