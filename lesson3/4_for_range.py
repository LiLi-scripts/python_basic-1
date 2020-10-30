"""
    Для генерации числовых последовательностей используется функция range()

    range(start[, end[, step])

    В математике - последовательность [start; end) - т.е. end не включается
"""

range(10)  # 0 1 2 3 4 5 6 7 8 9
range(1, 10)  # 1 2 3 4 5 6 7 8 9
range(1, 10, 2)  # 1 3 5 7 9

print('range(10):', end=' ')
for i in range(10):
    print(i, end=', ')

print('range(1, 10):', end=' ')
for i in range(1, 10):
    print(i, end=', ')

print('range(10, 1, -2):', end=' ')
for i in range(10, 1, -2):
    print(i, end=', ')
