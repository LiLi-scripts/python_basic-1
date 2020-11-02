str_1 = 'python'

str_2 = """python
asdas
as
d
asd
as
d
a"""

# "python" is the best language
str_3 = '"python" is the best language'
str_4 = "\"python\" is the best language"

# str_3 = "'python' is the best language"

print(str_1)
print(str_2)
print(str_3)
print(str_4)


# \n - перевод строки
# \t - табуляция

str_5 = '\tHello\nworld!'
print(str_5)

# префиксы r, f, b
str_6 = r'\tHello\nworld!'
print(str_6)

str_7 = '"python" is the best language "python" is the best language "python" is the best language "python" is the best language "python" is the best language '

str_7 = '"python" is the best language "python" is the best language' + \
    '"python" is the best language "python" is the best language' + \
    '"python" is the best language "python" is the best language'

str_7 = (
    '"python" is the best language "python" is the best language'
    '"python" is the best language "python" is the best language'
    '"python" is the best language "python" is the best language'
    '"python" is the best language "python" is the best language'
)
str_8 = """"python" is the best language "python" is the best language
"python" is the best language "python" is the best language
"python" is the best language "python" is the best language
"python" is the best language "python" is the best language
"""
print(7, str_7)
print(8, str_8)
