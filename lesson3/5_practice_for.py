"""
    Возведение чисел в степень до заданного предела.
"""

p = int(input('Введите степень: '))
limit = int(input('Предел: '))


number = 1
while number ** p < limit:
    print(number ** p, end=' ')
    number += 1
