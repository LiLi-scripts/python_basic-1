"""
    Написать функцию, которая по аналогии с вычисление факториала
    считает сумму числового рядо от 1 до n
"""

def sum_(n):
    if n == 1:
        return n
    return n + sum_(n - 1)

sum_(5) # 25


"""
    Написать функцию, которая возводит число a в степень b.
"""

def pow(a, b):
    return a ** b

print(pow(5, 2))  # 25
print(pow(4, 3))  # 64


"""
    Написать функцию capitalize, которая
    возводит 1 букву строки в верхний регистр, а все остальные в нижний.

    # ''.capitalize()
    # 'hello world' >> 'Hello world'
    # 'hello WoRld' >> 'Hello world'
    # 'HeLLo WoRld' >> 'Hello world'
"""

def capitalize(string):
    return string[0].upper() + string[1:].lower()

cap = capitalize  # cap - ссылка на функцию capitalize

print(cap('hello world'))  # 'Hello world'
print(cap('hello WoRld'))  # 'Hello world'
print(cap('HeLLo WoRld'))  # 'Hello world'
