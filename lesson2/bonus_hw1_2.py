# 2.
# Программа принимает на ввод 3 значения.
# Если все значения – числа, тогда вывести самое большое и самое маленькое из них,
# иначе вывести все значения.

a = input('a: ')
b = input('b: ')
c = input('c: ')

try:
    a, b, c = int(a), int(b), int(c)
except ValueError:
    print(a, b, c)
else:
    if a <= b <= c:
        print('max =', a, '; min =', c)
    elif a <= c <= b:
        print('max =', a, '; min =', b)
    elif b <= a <= c:
        print('max =', b, '; min =', c)
    elif b <= c <= a:
        print('max =', b, '; min =', a)
    elif c <= b <= a:
        print('max =', c, '; min =', a)
    else:
        print('max =', c, '; min =', b)
