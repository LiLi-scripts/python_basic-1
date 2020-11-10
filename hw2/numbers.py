"""
    Дано число от 1 до 999.
    1. Найти сумму цифр числа. (для 2-знач числа - lesson1/3_practice_operators.py)
    2. Вывести, в каком порядке расположены цифры (возрастания/убывания/в разброс)
"""

# Ниже описан один из вариантов решения задачи.

number = int(input())

if 1 <= number < 10:  # number >= 1 and number < 10
    print('sum =', number)
elif 10 <= number < 100:
    digit_1 = number // 10
    digit_2 = number % 10

    print('sum =', digit_1 + digit_2)

    if digit_1 < digit_2:
        print('increase')
    elif digit_1 > digit_2:
        print('decrease')
    else:
        print('equal')
elif 100 <= number < 1000:
    digit_1 = number // 100
    digit_2 = number // 10 % 10
    digit_3 = number % 10

    print('sum =', digit_1 + digit_2 + digit_3)

    if digit_1 < digit_2 < digit_3:
        print('increase')
    elif digit_1 > digit_2 > digit_3:
        print('decrease')
    elif digit_1 == digit_2 == digit_3:
        print('equal')
    else:
        print('random')
else:
    print('number must be from 1 to 999')
