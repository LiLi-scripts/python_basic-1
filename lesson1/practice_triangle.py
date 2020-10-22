"""
    Программа принимает на ввод 2 катета.
    Вычислить периметр и площадь прямугольного треугольника.
    a**2 + b**2 == c**2
"""

a = int(input('side a: '))
b = int(input('side b: '))

c = (a**2 + b**2)**0.5
print('side c:', c)

perimeter = a + b + c
area = a * b / 2

print('P =', perimeter)
print('S =', area)
