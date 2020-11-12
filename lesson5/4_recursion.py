"""
    Рекурсия.

    Вызов функции из нее же самой называется рекурсией.

    Одним из примеров практического применения рекурсии -
        алгоритм вычисления факториала.

"""

# факториал числа 5 - 1 * 2 * 3 * 4 * 5 = 120

n = int(input('n: '))

def fact(n):
    if n == 0:  # если n == 0 - возвращаем 1, так как факториал числа 0 = 1
        return 1
    # вызываем функцию с числом n, каждый раз уменьшая его на 1 и усножаем на n
    return fact(n - 1) * n

res = fact(5)
print(res)