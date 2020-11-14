"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

import re

input_number = input('Enter phone number: ')

number = ''
for digit in input_number:
    if digit.isdigit():
        number += digit

number = '380' + number[-9:]
if len(number) != 12:
    print('Wrong phone number. Please re-enter.')
else:
    print(number)

# P.S. строки 14-17 можно заменить 1 строкой с использованием re.sub
# number = re.sub(r'\D', '', input_number)
