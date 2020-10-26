"""
    try-except используется для перехвата исключений,
    чтоб программа могла работать дальше даже при возникновении ошибки.
"""

a = float(input())
b = float(input())

# минимальный рабочий код - использование блока try и except
try:
    print(a / b)
except:
    pass

# так же можно обратывать конкретные исключения и использовать доп блоки else и finally
try:
    print(a / b)
except ZeroDivisionError:
    print('zero div')
except Exception as e:
    print(e)
else:
    # выполнится, если не было ни одной ошибки
    print('else')
finally:
    # выполнится в любом случае
    print('finally')

print('end')
