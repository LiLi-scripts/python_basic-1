colors = ['red', 'yellow', 'orange', 'green', 'blue', 'violet']

# Цикл проходит по каждому элементу списка colors и выполняет тело цикла
for color in colors:
    # тело цикла

    if 'a' in color:
        continue
    elif 'b' in color:
        break

    print(color)
else:
    # если цикл был закончен не с помощью break, то выполняется этот блок
    print('"b" not found in any elements')

# оператор вхождения -- in
print('a' in ['ah', 'd', 'j', 'y', 'o'])
print('a' in ['a', 'd', 'j', 'y', 'o'])


number = [1,2,3,4,5,6]

for i in number:
    print(i*2)
