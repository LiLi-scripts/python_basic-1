"""
    Цикл while.
    Тело цикло выполняется до тех пор, пока выполняется условие.

    while условие:
        выполняемый код

    После каждого прохода тела цикла (итерация) условие снова проверяется.
"""

number = 1

while number < 10:

    if number == 3:
        number += 1
        # оператор continue прерывает текущую итерацию
        continue

    print(number)
    number += 1
else:
    # блок else выполняется в том случае, если цикл не был прерван break
    print('else')

print('out of while')
