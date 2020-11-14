"""
    1. Записать в файл practice.txt: числа от 9 до 17 через пробел  mode = 'w'
    2. Прочитать этот файл и вывести содержимое и тип содержимого на экран  mode = 'r'
    3. В файл с новой строки записать такой текст: Some text 123, @!$!@SA  mode = 'a'

    4. Прочитать файл и вывести в консоль: mode = 'r'
        - количество заглавных букв.  isupper()
        - количество строчных букв.   islower()
        - количество цифр.            isdigit()
        - количество спецсимволов.    string.punctuation
"""

import string

with open('practice.txt', 'w') as f:
    for num in range(9, 18):
        if num != 17:
            f.write(str(num) + ' ')
        else:
            f.write(str(num))
        # либо вариант с print()
        # if num != 17:
        #     print(num, end=' ', file=f)
        # else:
        #     print(num, end='', file=f)

with open('practice.txt') as f:
    print(f.read())

with open('practice.txt', 'a') as f:
    f.write('\nSome text 123, @!$!@SA')

u_counter = l_counter = d_counter = s_counter = 0

with open('practice.txt') as f:
    data = f.read()
    for i in data:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        elif not i.isspace():
            s_counter += 1
        # elif i in string.punctuation:
        #     s_counter += 1

print(u_counter, l_counter, d_counter, s_counter)
