"""
    Файлы.
"""

test_file = open('test.txt', 'r')  # r w a

print(test_file.tell())
print(test_file.read())

test_file.seek(15)
print(test_file.tell())
print(test_file.read())

test_file.seek(0)
print(test_file.readline())
print(test_file.readlines())

test_file.close()


with open('hello.txt', 'w') as f:
    # print(f.read())
    f.write('hello world!')
    print('hello world!', file=f)
