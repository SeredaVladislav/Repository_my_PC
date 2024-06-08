# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ list (Списки) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Изменяемый;
# Не хэшируемый;
# Последовательный;
# Итерируемый.


a = []  # Пустой список

numbers_list: list = [2, 4, 6, 8, 10]  # Список из чисел (int)
example_list: list = ['a', 'b', 'c', 'd']  # Список из строк (str)

# Индексы:
print(example_list[0])  # Нулевой (первый символ) элемент списка 'a';
print(example_list[1])  # Первый (второй символ) элемент списка 'b';
print(example_list[4])  # IndexError: list index out of range
print(example_list[-1])  # Последний элемент списка 'd'

# Срезы:
example_list_4: list = ['a', 'b', 'c', 'd', 'error', '_', 'temp_var']
print(example_list_4[:])  # [‘a’, ‘b’, ‘c’, ‘d’, ‘error’, ‘_’, ‘temp_var’]
print(example_list_4[2:])  # [‘c’, ‘d’, ‘error’, ‘_’, ‘temp_var’]
print(example_list_4[:3])  # [‘a’, ‘b’, ‘c’]
print(example_list_4[1:4])  # [‘b’, ‘c’, ‘d’];
print(example_list_4[::2])  # [‘a’, ‘c’, ‘error’, ‘temp_var’] # через 1 элемент;
print(example_list_4[::-1])  # [‘temp_var’, ‘_’, ‘error’, ‘d’, ‘c’, ‘b’, ‘a’] # создавая новый список в памяти;
print(str(example_list_4)[1:-1])  # 'a', 'b', 'c', 'd', 'error', '_', 'temp_var'.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Методы для list ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы списков, изменяют список, результат выполнения не нужно записывать в эту переменную.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .append()
# Добавление элемента в конец списка.
# Эквивалент: [len(a):] = [x]


example_list: list = ['a', 'b', 'c', 'd']

# Добавление строки str:
example_list.append('error')  # ['a', 'b', 'c', 'd', 'error']

# Добавление числа int:
example_list.append(5)  # ['a', 'b', 'c', 'd', 'error', 5]

# Добавление списка содержащего числа list(int):
example_list.append([123])  # ['a', 'b', 'c', 'd', 'error', 5, [123]]

# Добавление списка содержащего строки list(str):
example_list.append(['a', 'b'])  # ['a', 'b', 'c', 'd', 'error', 5, [123], ['a', 'b']]

# Добавление вещественного числа (float):
example_list.append(30.7)  # ['a', 'b', 'c', 'd', 'error', 5, [123], ['a', 'b'], 30.7]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .extend()
# Добавление (объединение) нового списка в текущий.


example_list_2: list = [7, 3, 3]
example_list: list = ['a', 'b', 'c', 'd']

# Добавление (объединение) списка с элементами в список example_list_2:
example_list_2.extend([4, 5])
print(example_list_2)  # [7, 3, 3, 4, 5]

# Объединение списков через конкатенацию:
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
print(example_list + example_list_2)  # ['a', 'b', 'c', 'd', 'error', 5, [123], ['a', 'b'], 30.7, 7, 3, 3, 4, 5]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .insert()
# Добавление нового объекта в список, перед указанным индексом.


names = ['Gvido', 'Roman', 'Timur']
example_list_2: list = [7, 3, 3]

names.insert(0, 'Anders')
print(names)  # ['Anders', 'Gvido', 'Roman' , 'Timur']

names.insert(3, 'Josef')
print(names)  # ['Anders', 'Gvido', 'Roman' , 'Josef', 'Timur']

example_list_2.insert(4, 'ex')
print(example_list_2)  # [7, 3, 3, 4, 'ex', 5]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .copy()
# Создает поверхностную копию списка.
# Эквивалент: a[:]


names = ['Gvido', 'Roman', 'Timur']

# Создание поверхностной копии списка names:
names_copy = names.copy()  # ['Gvido', 'Roman', 'Timur']


# Эквивалент:
names = ['Gvido', 'Roman', 'Timur']

# Создание поверхностной копии списка с помощью функции list():
names_copy1 = list(names)

# Создание поверхностной копии списка с помощью среза [:]:
names_copy2 = names[:]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .pop()
# Удаление элемента по индексу. (И возвращение его)
# Без аргумента удаляет последний элемент.


example_list_2: list = [7, 3, 3, 4, 'ex', 5]
example_list_2.pop()  # [7, 3, 3, 4, 'ex']

# Удаление по индексу:
example_list.pop(0)  # [3, 3, 4, 'ex']


names = ['Gvido', 'Roman', 'Timur']
# Сохранение удаленного элемента в переменной:
item = names.pop(1)  # Roman
print(names)  # ['Gvido', 'Timur']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .remove()
# Удаление, первого в очереди, указанного элемента.


example_list_3 = [1, 2, 3, 4, 5, 6, 7, 2]
example_list_3.remove(2)  # [1, 3, 4, 5, 6, 7, 2]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Инструкция del x[i]
# Удаляет элемент из списка по индексу.


example_list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Удаляет элемент 5-го индекса:
del example_list_10[5]  # [1, 2, 3, 4, 5, 7, 8, 9]

# Удаляет элементы по срезу индексов:
del example_list_10[2:7]  # [1, 2, 9]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .clear()
# Удаляет все элементы из списка.
# Эквивалент: del a[:]


names = ['Gvido', 'Roman', 'Timur']
names.clear()  # []


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .index()
# Возвращает первый, в последовательности, индекс указанного элемента.


example_list_5 = [4, 7, 5, 4, 10, 4]
print(example_list_2.index(4))  # 0


names = ['Gvido', 'Roman', 'Timur']
# Сохранение номера индекса в переменную:
position = names.index('Timur')  # 2


# Изменение элемента по индексу:
example_l = [4, 7, 5, 4, 10, 4]
example_l[1] = 'fish'  # [4, 'fish', 5, 4, 10, 4]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .count()
# Возвращает количество вхождений элемента в список по имени.


example_list_6 = [4, 7, 5, 4, 10, 4]
print(example_list_6.count(4))  # 3


names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')  # 3
cnt2 = names.count('Gvido')  # 1
cnt3 = names.count('Josef')  # 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .sort()
# list.sort(key=None, reverse=False). Сортирует элементы в ТЕКУЩЕМ списке по возрастанию..
# reverse=True для сортировки в обратном порядке.
# Сложность алгоритма составляет O(n log^n).

example_list_7 = [3, 7, 4, 2]
example_list_7.sort()
print(example_list_7)  # [2, 3, 4, 7]

list_num = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
a.sort()
print(list_num)  # [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]

# Сортирует список по убыванию:
example_list_7.sort(reverse=True)
print(example_list_2)  # [7, 4, 3, 2]

list_num.sort(reverse=True)
print(list_num)  # [1000, 99, 45, 34, 12, 9, 8, 7, 6, 1, 0, -2, -3, -67]

# Сортировка списка со строками:
list_names = ["Стив", "Рейчел", "Майкл", "Адам", "Джессика", "Лестер"]
list_names.sort()
print(list_names)  # ['Адам', 'Джессика', 'Лестер', 'Майкл', 'Рейчел', 'Стив']

list_symbol = ['бета', 'альфа', 'дельта', 'гамма']
list_symbol.sort()
print(list_symbol)  # ['альфа', 'бета', 'гамма', 'дельта']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Функция sorted()
# Синтаксис: sorted(iterable, key=None, reverse=False)
# Функция возвращает НОВЫЙ отсортированный список (всегда!), полученный из итерируемого объекта,
# который был передан как аргумент.

# Флаг reverse= позволяет управлять порядком сортировки. По умолчанию сортировка будет по возрастанию элементов.
# Указав флаг reverse=, можно поменять порядок.

# С помощью параметра key= можно указывать, как именно выполнять сортировку. Параметр key= ожидает функцию,
# с помощью которой должно быть выполнено сравнение.

# Например, таким образом можно отсортировать список строк по длине строки:
list_of_words = ['one', 'two', 'list', '', 'dict']
new_list_of_words = sorted(list_of_words, key=len)
print(new_list_of_words)  # ['', 'one', 'two', 'list', 'dict']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .reverse()
names = ['Gvido', 'Roman', 'Timur']
# Реверсирует тот же список, не создавая новый, в отличие от среза[::-1]:
names.reverse()
print(names)  # ['Timur', 'Roman', 'Gvido']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Вхождение элементов в список
example_list_8 = [2, 3, 4, 1, 32]
print(2 in example_list_8)  # True
print(33 not in example_list_8)  # True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Функции min(), max(), sum()
# Наибольший элемент в списке:
print(max(example_list_8))  # 32

# Наименьший элемент в списке:
print(min(example_list_8))  # 1

# Сумма чисел в списке:
print(sum(example_list_8))  # 42

# Для списка строк:
example_list_9 = ['a', 'b', 'c']
print(max(example_list_9))  # c
print(min(example_list_9))  # a
print(sum(example_list_9))  # TypeError: unsupported operand type(numbers_pairs) for +: 'int' and 'str'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Списочное выражение (list comprehension) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

numbers = []  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10):
    numbers.append(i)

# List comprehension:
numbers = [i for i in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zeros = [0 for i in range(10)]  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

squares = [i ** 2 for i in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cubes = [i ** 3 for i in range(10, 21)]  # [1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]

chars = [c for c in 'abcdefg']  # ['a', 'b', 'c', 'd', 'error', 'finish', 'flag']

numbers5 = [i * j for i in range(1, 5) for j in range(2)]  # [0, 1, 0, 2, 0, 3, 0, 4]

evens = [i for i in range(21) if i % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Вложенный список:
n = 4  # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]  # создаем список из элементов строки
    my_list.append(elem)

print(my_list)
