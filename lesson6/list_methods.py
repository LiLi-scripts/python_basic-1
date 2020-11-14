"""Встроенные методы списков"""

my_list = [1, 'some', 'black', 8.7, 1, 'python']
print('1.', my_list)

# Добавление элемента -- append(object)

my_list.append('some') # элемент добавляется в конец списка
print('2.', my_list)


# Вставка элемент -- insert(index, object)

my_list.insert(0, 'pre') # по индексу 0 вставляем единичку
print('3.', my_list)


# Вставка нескольких элементов ( списка ) -- extend([])

my_list.extend(['red', 34, 'python']) # элементы добавляются в конец списка
print('4.', my_list)

# Удаление элемента списка -- remove(object)

my_list.remove('python') # удаляет первое вхождение 'red'
print('4.', my_list)

# Удаление элемента списка -- pop([index]) , по умолчанию удаляет последний элемент

my_list.pop() # удаляет последний элемент
my_list.pop(0) # удаляет элемент с индексом 0
print('5.', my_list)

# Очищение списка -- clear()

my_list_to_clear = my_list[:] # создали копию нашего списка (чтоб не трогать основной)

my_list_to_clear.clear() # очищаем список

print('6.', my_list_to_clear)


# Получить индекс объекта -- index(object)

print('7.', my_list.index('red'))

# Число вхождений объекта -- count(object)

print('8.', my_list.count('some'))

# Сортировка списка -- sort() изменяет список, в отличии от sorted()

second_list = [5, -2, 3, -9, 10]

print('9.', second_list)
second_list.sort()
print('10.', second_list)

# Реверс -- reverse() (элементы в обратном порядке)

second_list.reverse()
print('11.', second_list)
