"""
    Написать программу, которая принимает строку
    и выводит строку без пробелов и ее длину.
"""


def main():
    string = input('Enter a string: ')

    string = cut_space(string)

    print(string, len(string))


def cut_space(string):
    return string.replace(' ', '')

main()
