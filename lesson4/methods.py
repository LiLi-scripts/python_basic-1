# методы строк

s = 'Hello world!'

# работа с регистром upper, lower, title, capitalize, swapcase
print(s)
print(s.upper())  # к верхнему регистру
print(s.lower())  # к нижнему регистру
print(s.title())  # первую букву каждого слова к верхнему регистру
print(s.capitalize())  # Первый символ к верхнему, остальные к нижнему
print(s.swapcase())  # Меняет регистр на противоположный

# Индекс первого вхождения элемента. Если не найдено - вернет -1

# index и rindex работают так же, только вызывают ValueError, если элемент не найден
print(s.find('l'))  # слева направо
print(s.rfind('l'))  # справа налево
print(s.index('l'))

# удаление пробельных символов strip, lstrip, rstrip

# проверка символов. isdigit, isalpha, isnumeric, isalnum
print('123'.isdigit())  # состоит ли строка только из цифр
print('½'.isnumeric())  # состоит ли строка только из цифр
print('123'.isalpha())  # только из букв

# isupper, islower, istitle, isspace

print(s.startswith('Hello')) # начинается ли строка с 'Hello'
print(s.endswith('!'))  # заканчивается ли строка '!'

# разбиение строки по разделителю split
# склеивание строки с разделителем join

print(s.split('o'))
print('-------'.join(s.split('o')))

# Замена шаблона
print(s.replace('world', 'python'))

print(s.ljust(20, '!')) # делает длину строки не меньше 20, по необходимости заполняя последние символы '!'
print(s.rjust(20)) # делает длину строки не меньше 20, по необходимости заполняя первые символы '!'

print(s.center(20, '!')) # центрирует строку
