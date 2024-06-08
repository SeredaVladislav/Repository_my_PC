# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Словарь(dict) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Изменяемый контейнерный объект;
# Ключ словаря - неизменяемое (хэшируемое) значение;
# Индексируемые с помощью ключей;
# Словарь — реализация структуры данных "ассоциативный массив" или "хеш таблица"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Создание словаря ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

info = dict(name='Timur', age=28, job='Teacher')

# Создание словаря на основании списков и кортежей:
info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
info_dict = dict(info_list)  # создаем словарь на основе списка кортежей

info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
info_dict2 = dict(info_tuple)  # создаем словарь на основе кортежа списков

# Метод .fromkeys()
# Позволяет создать словарь с несколькими ключами для одного значения:
dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')

# Создание пустого словаря:

dict3 = {}
dict4 = dict()

print(dict3)  # {}
print(dict4)  # {}

# Функция-упаковщик zip()
# Позволяет создать словарь на основании двух списков (кортежей):

keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']

info2 = dict(zip(keys, values))
print(info)  # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Функции для словаря ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Функция len()
fruits = {'Apple': 70, 'Grape': 100, 'Banana': 80}
capitals = {'Россия': 'Москва', 'Франция': 'Париж'}

print(len(fruits))  # 3
print(len(capitals))  # 2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Оператор принадлежности in
# Проверка наличия ключа в словаре:
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

if "Россия" in capitals:
    print("В словаре есть ключ Россия")

# Проверка наличия значения в словаре:
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

if "Париж" in capitals.values():
    print("В словаре есть значение Париж")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Встроенные функции sum(), min(), max():

# Функция sum() принимает в качестве аргумента словарь с числовыми ключами и вычисляет сумму его ключей.
my_dict = {10: 'Россия', 20: 'США', 30: 'Франция'}
print('Сумма всех ключей словаря =', sum(my_dict))  # Сумма всех ключей словаря = 60

# Функции min() и max() принимают в качестве аргумента словарь и находят минимальный и максимальный ключ соответственно,
# при этом ключ может принадлежать к любому типу данных, для которого возможны операции порядка <, <=, >, >=
# (числа, строки, и т.д.)

capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
months = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
print('Минимальный ключ =', min(capitals))  # Минимальный ключ = Россия
print('Максимальный ключ =', max(months))  # Максимальный ключ = 3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Оператор принадлежности in
months1 = {1: 'Январь', 2: 'Февраль'}
months2 = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
months3 = {3: 'Март', 1: 'Январь', 2: 'Февраль'}

print(months1 == months2)  # False
print(months2 == months3)  # True
print(months1 != months3)  # True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Методы словарей ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# метод items() – возвращает словарные пары ключ: значение, как соответствующие им кортежи;
# метод keys() – возвращает список ключей словаря;
# метод values() – возвращает список значений словаря.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Добавление и изменение элементов в словаре: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
info = {
    'name': 'Sam',
    'age': 28,
    'job': 'Teacher'
}

info['name'] = 'Timur'  # изменяем значение по ключу name
info['email'] = 'timyr-guev@yandex.ru'  # добавляем в словарь элемент с ключом email
print(info)  # {'name': 'Timur', 'age': 28, 'job': 'Teacher', 'email': 'timyr-guev@yandex.ru'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод get()
# Синтаксис: get('key', 'Необязательный аргумент - Комментарий при отсутствии ключа')
# Не возвращает ошибку, если в словаре нет ключа, а выводит None, так же выводит указанное значение
# при внесении второго аргумента:

info = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev'
}

item1 = info.get('salary')
item2 = info.get('salary', 'Информации о зарплате нет')
print(item1)  # None
print(item2)  # Информации о зарплате нет

# Пример:
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1  # добавляет в словарь значение по ключу из списка количество повторений.

# Яркое применение метода get():
num = int(input())
if num == 1:
    description = 'One'
elif num == 2:
    description = 'Two'
elif num == 3:
    description = 'Three'
else:
    description = 'Unknown'
print(description)

# Вместо нескольких вложенных условных конструкций:
num = int(input())
description = {1: 'One', 2: 'Two', 3: 'Three'}
print(description.get(num, 'Unknown'))  # Либо возвращает значение по ключу, либо Unknown

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод update()
# Объединяет словари. При одинаковых ключах, остается тот что в аргументе метода update()
# Эквивалент метода: | и |=

info1 = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev'
}

info2 = {
    'age': 30,
    'city': 'New York',
    'email': 'bob@web.com'
}

info1.update(info2)
print(info1)  # {'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод setdefault()
# Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент
# словаря, если он отсутствует.

info = {
    'name': 'Bob',
    'age': 25
}

name1 = info.setdefault('name')  # параметр default не задан
name2 = info.setdefault('name', 'Max')  # параметр default задан
print(name1)  # Bob
print(name2)  # Bob

# Если ключ отсутствует, то он создается и присваивается 2-й переданный аргумент. Либо None, если не передан.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Удаление элементов из словаря ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Существует несколько способов удаления элементов из словаря:
# оператор del;
# метод pop();
# метод popitem();
# метод clear().


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Оператор del
# С помощью оператора del можно удалять элементы словаря по определенному ключу. (либо ошибка, если нет ключа)

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

del info['email']  # удаляем элемент имеющий ключ email
del info['job']  # удаляем элемент имеющий ключ job
print(info)  # {'name': 'Sam', 'age': 28}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод pop()
# С помощью оператора pop() можно удалять элементы словаря по определенному ключу и возвратить его значение.

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

email = info.pop('email')  # удаляем элемент по ключу email, возвращая его значение
job = info.pop('job')  # удаляем элемент по ключу job, возвращая его значение

print(email)  # timyr-guev@yandex.ru
print(job)  # Teacher
print(info)  # {'name': 'Sam', 'age': 28}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод popitem()
# Метод удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение).

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info['surname'] = 'Sinclar'

item = info.popitem()

print(item)  # ('surname', 'Sinclar')
print(info)  # {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод clear()
# Метод удаляет все элементы словаря.

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info.clear()  # {}
print(info)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод copy()
# Метод создает поверхностную копию словаря.

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info_copy = info.copy()
print(info_copy)  # {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Метод copy() отличается от присвоения новой переменной ссылки на старый словарь.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Перебор элементов словаря ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

for key in capitals:
    print(key)

# Россия
# Франция
# Чехия

# Для вывода элементов словаря каждого на отдельной строке:
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

for key in capitals:
    print("Столица", key, "- это", capitals[key])

# Столица Россия - это Москва
# Столица Франция - это Париж
# Столица Чехия - это Прага

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы keys(), values(), items():

# Словарные методы items(), keys(), values() возвращают не совсем обычные списки.
# Типы этих списков -  dict_items, dict_keys, dict_values соответственно, в отличие от обычных списков
# list. Методы обычных списков недоступны для списков типа dict_items, dict_keys, dict_values.
# Явное преобразование с помощью функции list() для получения доступа к методам списков.

# Метод keys() возвращает список ключей всех элементов словаря (итерация по ключам):
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

for key in capitals.keys():
    print(key)

# Россия
# Франция
# Чехия

# Метод values() возвращает список значений всех элементов словаря (итерация по значениям):
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

for value in capitals.values():
    print(value)

# Москва
# Париж
# Прага

# Метод items() возвращает список всех элементов словаря, состоящий из кортежей пар (ключ, значение):
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}

for item in capitals.items():
    print(item)

# ("Россия", "Москва")
# ("Франция", "Париж")
# ("Чехия", "Прага")

capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}
for key, value in capitals.items():
    print(key, "-", value)

# Россия - Москва
# Франция - Париж
# Чехия - Прага

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Распаковка ключей словаря

capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}
print(*capitals, sep="\n")

# Россия
# Франция
# Чехия

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Сортировка словаря:
# Функция sorted()

# Сортировка по ключам:
capitals = {
    "Россия": "Москва",
    "Англия": "Лондон",
    "Чехия": "Прага",
    "Бразилия": "Бразилиа",
}
for key in sorted(capitals):  # в алфавитном порядке
    print(key)

# Англия
# Бразилия
# Россия
# Чехия

# Сортировка по значениям:
# При сортировке словаря по значениям мы используем анонимную функцию lambda x: x[1]
capitals = {
    "Россия": "Москва",
    "Англия": "Лондон",
    "Чехия": "Прага",
    "Бразилия": "Бразилиа",
}
for key, value in sorted(capitals.items(), key=lambda x: x[1]):
    print(value)


# Бразилиа
# Лондон
# Москва
# Прага

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Задачи ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def information_for_students(num_course: str) -> str:
    """
    Напишите программу, которая по номеру курса выводит информацию о данном курсе.
    """

    course_info: dict = {
        "CS101": (3004, "Хайнс", "8:00"),
        "CS102": (4501, "Альварадо", "9:00"),
        "CS103": (6755, "Рич", "10:00"),
        "NT110": (1244, "Берк", "11:00"),
        "CM241": (1411, "Ли", "13:00")
    }
    result_info: str = ", ".join(map(str, course_info[num_course]))

    return f"{num_course}: {result_info}"


if __name__ == '__main__':
    number_course: str = input()
    print(information_for_students(number_course))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def translit_numbers(num: str) -> None:
    """
    Напишите программу, которая будет превращать натуральное число в строку,
    заменяя все цифры в числе на слова.
    """
    control_values: dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    for one_num in num:
        print(control_values[int(one_num)], end=" ")
    print()


if __name__ == '__main__':
    number: str = input()
    translit_numbers(number)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
users_data = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
    {'name': 'John', 'phone': '233-421-32', 'email': ''},
    {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
    {'name': 'Alina', 'phone': '+7948-799-2434'},
    {'name': 'Robert', 'phone': '420-2011', 'email': ''},
    {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
    {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
    {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
    {'name': 'Roman', 'phone': '+7459-145-8059'},
    {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}
]


def users_without_email(users: list[dict]) -> list[str]:
    """
    Функция для вывода имен всех пользователей (в алфавитном порядке),
    у которых нет информации об электронной почте.
    """

    name_array = []

    for user in users:
        if 'email' not in user or user['email'] == '':
            name_array.append(user['name'])

    return sorted(name_array)


if __name__ == '__main__':
    func = users_without_email(users_data)
    print(*func)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Печать на кнопочном телефоне:
keyboard_phone = {
    1: ".,?!:",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
    0: " "
}

enter_text = input().upper()
numbers_keyboard_phone = []

for word in enter_text:
    for key, value in keyboard_phone.items():
        if word in value:
            index_value = value.find(str(word)) + 1
            numbers_keyboard_phone.extend(str(key) * index_value)

print("".join(numbers_keyboard_phone))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Объединение словарей, с суммой значений одинаковых ключей"""
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
result.update(dict1)

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)
# {'a': 400, 'z': 999, 'b': 400, 'c': 312, 'd': 445, 'e': 98, 't': 853, 'q': 34, 'f': 90, 'm': 230, 'p': 123, 'w': 111}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" Чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
 должно быть выведено то, что меньше в лексикографическом порядке. """

s = ('orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana'
     ' banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes'
     ' melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince'
     ' grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince'
     ' lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana'
     ' banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate'
     ' barley plum banana quince barley lime grapefruit pomegranate barley').split()

dict_array = {word: s.count(word) for word in s}
repeat_word = [key for key, value in dict_array.items() if value == max(dict_array.values())]
print(min(repeat_word))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" Создать словарь, который будет хранить в виде кортежа с (Ф.И., возраст хозяина): [Клички собаки хозяина] """

pets = [
    ('Hatiko', 'Parker', 'Wilson', 50),
    ('Rusty', 'Josh', 'King', 25),
    ('Fido', 'John', 'Smith', 28),
    ('Butch', 'Jake', 'Smirnoff', 18),
    ('Odi', 'Emma', 'Wright', 18),
    ('Balto', 'Josh', 'King', 25),
    ('Barry', 'Josh', 'King', 25),
    ('Snape', 'Hannah', 'Taylor', 40),
    ('Horry', 'Martha', 'Robinson', 73),
    ('Giro', 'Alex', 'Martinez', 65),
    ('Zooma', 'Simon', 'Nevel', 32),
    ('Lassie', 'Josh', 'King', 25),
    ('Chase', 'Martha', 'Robinson', 73),
    ('Ace', 'Martha', 'Williams', 38),
    ('Rocky', 'Simon', 'Nevel', 32)
]

result = {}
for pet in pets:
    result.setdefault(pet[1:], []).append(pet[0])

print(result)
# {
# ('Parker', 'Wilson', 50): ['Hatiko'],
# ('Josh', 'King', 25): ['Rusty', 'Balto', 'Barry', 'Lassie'],
# ('John', 'Smith', 28): ['Fido'],
# ('Jake', 'Smirnoff', 18): ['Butch'],
# ('Emma', 'Wright', 18): ['Odi'],
# ('Hannah', 'Taylor', 40): ['Snape'],
# ('Martha', 'Robinson', 73): ['Horry', 'Chase'],
# ('Alex', 'Martinez', 65): ['Giro'],
# ('Simon', 'Nevel', 32): ['Zooma', 'Rocky'],
# ('Martha', 'Williams', 38): ['Ace']
# }

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Аннаграммы 2 строк"""
w1, w2 = ["".join(sorted(map(str, input().lower()))).strip().strip(".,!?:;-") for _ in range(2)]
print(("NO", "YES")[w1 == w2])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""На вход программе подается список стран и городов каждой страны. Затем даны названия городов. 
Напишите программу, которая для каждого города выводит, в какой стране он находится."""

initial_data = [input().split() for _ in range(int(input()))]
city_data = [input() for _ in range(int(input()))]

dictionary_counter_city = {i[0]: i[1:] for i in initial_data}

for city in city_data:
    for key, value in dictionary_counter_city.items():
        if city in value:
            print(key)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Вложенные словари, Генераторы словарей ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Вложенные словари ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Создание вложенных словарей.
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info2 = dict(emp1={'name': 'Timur', 'job': 'Teacher'},
             emp2={'name': 'Ruslan', 'job': 'Developer'},
             emp3={'name': 'Rustam', 'job': 'Tester'})

ids = ['emp1', 'emp2', 'emp3']
emp_info = [{'name': 'Timur', 'job': 'Teacher'},
            {'name': 'Ruslan', 'job': 'Developer'},
            {'name': 'Rustam', 'job': 'Tester'}]

info3 = dict(zip(ids, emp_info))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Обращение к элементам вложенного словаря.
info4 = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
         'emp3': {'name': 'Rustam', 'job': 'Tester'}}

print(info4['emp1']['name'])  # Timur
print(info4['emp2']['job'])  # Developer

# Вывод через метод .get(), без возникновения ошибки, при отсутствии ключа:
print(info4.get('emp1')['name'])  # Timur
print(info4.get('emp2')['job'])  # Developer

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Изменение вложенных словарей.
info5 = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
         'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info5['emp1']['job'] = 'Manager'

print(info5['emp1'])  # {'name': 'Timur', 'job': 'Manager'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Итерация по вложенным словарям.
info6 = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
         'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp in info6:
    print('Employee ID:', emp)
    for key in info6[emp]:
        print(key + ':', info6[emp][key])
    print()

# Employee ID: emp1
# name: Timur
# job: Teacher

# Employee ID: emp2
# name: Ruslan
# job: Developer

# Employee ID: emp3
# name: Rustam
# job: Tester

# Итерация с помощью метода .items():
info7 = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
         'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp, inf in info7.items():
    print('Employee ID:', emp)
    for key in inf:
        print(key + ':', inf[key])
    print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Генераторы словарей ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Пример генератора словаря, где ключ - число, значение - квадрат этого числа:
gen_dict = {i: i ** 2 for i in range(6)}
print(gen_dict)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Генератор словаря при итерировании по строке:
dct = {c: c * 3 for c in 'ORANGE'}
print(dct)  # {'O': 'OOO', 'R': 'RRR', 'A': 'AAA', 'N': 'NNN', 'G': 'GGG', 'E': 'EEE'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения:
lst = ['ReD', 'GrEeN', 'BlUe']
dct = {c.lower(): c.upper() for c in lst}
print(dct)  # {'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Извлечение из словаря элементов с определенными ключами:
dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]
dict2 = {k: dict1[k] for k in selected_keys}
print(dict2)  # {0: 'A', 2: 'C', 5: 'F'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Условия в генераторе словарей.

# Пример генератора словаря с условием, где ключ - четное число, значение - квадрат этого числа:
squares = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Альтернатива, с помощью среза:
squares = {i: i ** 2 for i in range(0, 10, 2)}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Генераторы вложенных словарей.
squares2 = {i: {j: j ** 2 for j in range(i + 1)} for i in range(5)}

for value in squares2.values():
    print(value)

# {0: 0}
# {0: 0, 1: 1}
# {0: 0, 1: 1, 2: 4}
# {0: 0, 1: 1, 2: 4, 3: 9}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
