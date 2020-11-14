# Создание списков (пустого и заполненного)

# Первый способ
my_list = []
my_list2 = [1, 'word', False, 2.0]

print(my_list)
print(my_list2)

# Второй способ
empty_list = list()
list_from_str = list('some list')

print(empty_list)
print(list_from_str)


colors = ['red', 'green', 'blue', 'yellow']

# Доступ к элементам списка по индексу, начиная с нуля (1й элемент - индект 0, 2й элемент - индекс 1 и т.д.)
# Положительный индекс - счет слева направо
print(colors[0])
print(colors[2])

# Отрицательный индекс - счет справа налево
print(colors[-1])


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Срезы [start:end:step]. Срез происходит с индекса start (включительно) до end (не включительно) с шагом end

print(letters[1:5:2])
print(letters[:5])

# Отрицательный шаг означает реверс, т.е. справа налево
print(letters[5:2:-1])
