# 1.
# дано 3 переменных. a , b , c
# a ==>>  a + b
# b ==>>  c - a
# c ==>>  a + b + c

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# множественное присваивание
a, b, c = a + b, c - a, a + b + c

print('a =', a, '; b =', b, '; c =', c)

#2.
# Дано число. Вывести такие его характеристики:
# ноль/не ноль , отрицательное/положительное , четное/нечетное

x = int(input())

if x == 0:
    print('zero')
elif x > 0:
    print('positive')
    if x % 2 == 0:
        print('even')
    else:
        print('odd')
else:
    print('negative')
    if x % 2 == 0:
        print('even')
    else:
        print('odd')
