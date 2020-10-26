"""
    Инструкция if-else имеет 2 варианта описания.
    1 - стандартный, 2 - строчный (обычно занимает 1 строку, но не обязательно)

    1.      if условие:
                True
            else:
                False

    2.      True if условие else False
"""

x = 0

# 1 вариант
if x > 0:
    answer = 'p'
elif x < 0:
    answer = 'n'
else:
    answer = 'zero'
print(answer)

# 2 вариант (эквивалентный 1)
answer = 'zero' if x == 0 else 'p' if x > 0 else 'n'
print(answer)
