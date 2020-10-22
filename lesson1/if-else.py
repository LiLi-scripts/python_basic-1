"""
    Инструкция if-else.
    Логические операторы: ==, !=, >, <, >=, <=.

    if a != b:  # если а не равно b
        pass
    else:  # иначе
        pass
"""

a = int(input('Enter a: '))
b = int(input('Enter b: '))

if a == b:
    print(a, '==', b)
elif a < b:
    print(a, '<', b)
else:
    print(a, '>', b)

print('code after if-else construction')
