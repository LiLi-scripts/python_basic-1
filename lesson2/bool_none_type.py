"""
    Логический тип данных bool
    Может быть True либо False

    Тип данных NoneType
    Для хранения пустых значений используется None.
"""

print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>

# bool находится в подмножестве int, поэтому преобразовывается в числа
# и для него доступны все арифметические операции, как и для чисел
print(int(True))  # 1
print(int(False))  # 0
print(True + True)  # 2
print(2 + True * False ** 0)  # 3

# bool и числа
# число 0 - это False, все остальные числа - True
a = 0
b = -123
print(bool(a))  # False
print(bool(b))  # True

# bool и последовательности (строки, списки, кортежи, множества, словари)
# пустая последовательность - это False, заполненная - True
print(bool(''))  # False
print(bool(' '))  # True
print(bool([0, 0, 0]))  # True
