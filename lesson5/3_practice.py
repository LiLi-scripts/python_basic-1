"""
    Необходимо написать программу, которая принимает на ввод 2 числа.
    Считает сумму числе в отдельной функции.
    Если сумма больше 0, то вызывается функция positive, которая выводит сообщение 'positive',
    усли меньше - функция negative, которая выводит сообщение negative.

"""


def main():
    a = int(input('a: '))
    b = int(input('b: '))

    result = summ(a, b)

    if result > 0:
        positive()
    elif result < 0:
        negative()


def summ(a, b):
    return a + b


def positive():
    print('positive')


def negative():
    print('negative')

main()
