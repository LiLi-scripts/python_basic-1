"""
    Найти факториал числа n.

    1 * 2 * 3 * 4 = 24
"""

n = int(input('n: '))

tmp = 1
while n > 1:
    tmp *= n
    n -= 1

print('factorial 4 =', tmp)


# Еще один вариант решения

# num = int(input("Enter: "))
# factorial = 1
# result = 1

# while factorial <= num:
#     result *= factorial
#     factorial += 1

# print(result)
