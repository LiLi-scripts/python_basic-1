"""
    Вывести количество дней в году, учитывая високосный год.
    (високосный год кратный 4, но не кратный 100 или кратный 400)
"""

# Ниже описаны одини из многих вариантов решения задачи.

year = int(input('year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('366')
else:
    print('365')

# вариант решения со строчным if-else
print('366' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '365')
