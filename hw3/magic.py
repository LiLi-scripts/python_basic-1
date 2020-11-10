"""
    Магическое число.
    При запуске программы генерируется число, которое нужно угадать.
    Подсказки: больше или меньше.
    Программа в бесконечном цикле.
    После отгадывания появляется результат: само число, количество попыток,
        а так же вопрос: "Continue? (y/n)"

    * Для генерации случайного числа можно воспользоваться
        функцией random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
"""

# Ниже описан один из вариантов решения задачи.

import random

random_number = random.randint(1, 100)  # случайное число от 1 до 100
counter = 0  # счетчик попыток
record_counter = 999  # рекордное число попыток
print('The game started. Guess the number.\n')

while True:
    try:
        number = int(input('Magic number is '))
        counter += 1
    except ValueError:
        continue

    if number > random_number:
        print('no, magic number less than', number)
    elif number < random_number:
        print('no, magic number greater than', number)
    else:
        print('\nCongratulations! Magic number is', number)
        if counter < record_counter:
            print('WOW, new record! Attempts: ', counter)
            record_counter = counter
        else:
            print('Attempts: ', counter)

        if input('\nContinue? (y/n) ') != 'y':
            break

        random_number = random.randint(1, 100)
        counter = 0
