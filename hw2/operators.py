"""
    Даны 3 челых числа.
    1. Найти сумму тех чисел, которые делятся на 5, иначе вывести сообщение.
    2. Найти количество положительных чисел.
    3. Найти количество отрицательных чисел.
    4. Найти сумму 2х найбольших чисел.

    Вывести сообщение типа:

    Числа: -10, 4, 21
    1. -10
    2. 2
    3. 1
    4. 25
"""

# Ниже описан один из вариантов решения задачи.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# 1.
summ = 0

if a % 5 == 0:
    summ += a

if b % 5 == 0:
    summ += b

if c % 5 == 0:
    summ += c

print('1.', summ)

# 2 and 3.
positive = 0
negavite = 0

if a > 0:
    positive += 1
elif a < 0:
    negavite += 1

if b > 0:
    positive += 1
elif b < 0:
    negavite += 1

if c > 0:
    positive += 1
elif c < 0:
    negavite += 1

print('2.', positive)
print('3.', negavite)

# 4.
if a >= b >= c or b >= a >= c:
    result = a + b
elif a >= c >= b or c >= a >= b:
    result = a + c
else:
    result = b + c

print('4.', result)
