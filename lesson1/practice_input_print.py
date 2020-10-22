"""
    Написать программу, которая принимает на ввод имя, город, возраст.
    И выводит текст, в формате:
    'Max from Kiev. He is 21.'
"""


name = input('Enter your name: ')
city = input('Enter your city: ')
age = input('Enter your age: ')

print(name, ' from ', city, '. He is ', age, '.', sep='')
print(name + ' from ' + city + '. He is ' + age + '.')
