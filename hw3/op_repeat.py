"""
    Программа принимает на ввод 5-ти значное число.
    Заменяет каждую вторую цифру на 0 и выводит результат.

    [in] 12345
    [out] 10305

    * Если введено не 5-ти значное число
        либо не число обработать и вывести соответствующее сообщение.
"""

# Ниже описан один из вариантов решения задачи.

try:
    n = int(input('Enter a five-digit number: '))
    if 9999 < n < 100000:
        result = n - n // 1000 % 10 * 1000 - n // 10 % 10 * 10
        print(result)
    else:
        print('Number must be five digits.')
except ValueError:
    print('This is not a number.')
