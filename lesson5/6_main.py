# import operations_module
# from operations_module import *
from operations_module import summ, mul, div

# импорт модуля из пакета
from packet import module1
# импорт функции из модуля, которых лежит в пакете
from packet.module1 import mul


def main():
    a = int(input('a: '))
    op = input('+ * /')
    b = int(input('b: '))

    if op == '+':
        result = summ(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        result = 0

    print(result)

main()
