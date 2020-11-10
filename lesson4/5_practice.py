"""
    1. Вводим строку.
    Вывести первые три символа в верхнем регистре и
    последние три символа в нижнем регистре, если длина строки больше 5.
    Иначе вывести первый символ с измененным регистром столько раз, какова длина строки.
"""

s = input('1. Enter some string: ')

if len(s) > 5:
    print(s[:3].upper(), s[-3:].lower())
else:
    print(s[0].swapcase() * len(s))

"""
    2. Определить, является ли строка палиндромом.
"""

s = input('2. Enter some string: ')

if s == s[::-1]:
    print('+')
else:
    print('-')


"""
    3. Удаление из строки повторяющихся символов и пробелов.

    for
    find()
"""

s = input('3. Enter some string: ')
new = ''

for elem in s:
    if new.find(elem) == -1 and elem != ' ':
        new += elem

    # if elem not in new and elem != ' ':
    #     new += elem

print(new)


"""
    4. Посчитать количество цифр, строчных и заглавных букв в строке.
"""

s = input('4. Enter some string: ')
count_d = count_u = count_l = 0

for i in s:
    if i.isdigit():
        count_d += 1
    elif i.islower():
        count_l += 1
    elif i.isupper():
        count_u += 1

print(count_d, count_l, count_u)
