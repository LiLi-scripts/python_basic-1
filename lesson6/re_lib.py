"""
    Библиотека re содержит функции для работы со строками
    с использованием регулярных выражений.

    Основные регулярные выражения:
    r'\d' - любая цифра
    r'\D' - любая не цифра
    r'\w' - любая буква либо цифра
    r'\W' - любая не буква и не цифра
    r'\s' - пробельный символ
    r'\s' - любой символ, кроме пробельных

    Так же помжно определять последовательности символов:
    r'[a-z]' - любая строчная буква от a до z
    r'[A-Z]' - любая заглавная буква от A до Z
    r'[0-9]' - любая цифра от 0 до 9
    r'[a-z0-9]' - любая строчная буква от a до z либо цифра от 0 до 9

    Определение количества символов:
    r'\d{2}' - последовательность 2х любых цифр
    r'[a-z]{5}' - последовательность 5х любых строчных букв
    r'[a-zA-Z]+' - последовательность больших и маленьких букв любой длины
                    (Можно использовать для поиска всех слов в предложении)
"""

import re

string = 'Hello world!'

# re.findall(pattern, string) # возвращает список всех найденных совпадений
result_1 = re.findall(r'world', string)
result_2 = re.findall(r'[a-z]', string)
print(result_1)  # ['world']
print(result_2)  # ['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

number = '+38 (073) 123-45-67'
all_digits = re.findall(r'\d', number)
print(all_digits)  # ['3', '8', '0', '7', '3', '1', '2', '3', '4', '5', '6', '7']
print(''.join(all_digits))  # 380731234567

# re.sub(pattern, repl, string) # ищет шаблон в строке и заменяет его на указанную подстроку
result = re.sub(r'world', 'friend', string)
print(result)

number = '+38 (073) 123-45-67'
formatted_number = re.sub(r'\D', '', number)
print(formatted_number)  # 380731234567


# re.search(pattern, string) # ищет первое вхождение заданого шаблона

result = re.search(r'world', string)
print(result.group())  # world
print(result.start())  # 6 (индекс начала шаблона в строке)
print(result.end())  # 11 (индекс окончания шаблона в строке)

# re.split(pattern, string, [maxsplit=0]) # работает как и str().split()

test_string = 'python0is1the2best3language'

result = re.split(r'\d', test_string)
print(result)  # ['python', 'is', 'the', 'best', 'language']

# собрать регулярное выражение в отдельный объект
# re.compile(pattern, repl, string)

pattern = re.compile(r'world')

result = pattern.findall(string)
# or
result = re.findall(pattern, string)

print(result) # ['world']


"""
    Дополнительные спецсимволы.
"""

string = 'Hello world123!'

result = re.findall(r'[a-zA-Z]+', string)
print(result)  # ['Hello', 'world']

result = re.findall(r'\d+', string)
print(result)  # ['123']
