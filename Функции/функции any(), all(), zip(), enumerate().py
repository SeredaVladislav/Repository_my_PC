# ---------------------------------------------- Функции all() и any() -------------------------------------------------
# -------------------------------
# ------------

# -------------------------------
# Функция all():

# Встроенная функция all() возвращает значение True, если все элементы переданной ей последовательности
# (итерируемого объекта) истинны (приводятся к значению True), и False в противном случае.

# Сигнатура функции следующая: all(iterable). В качестве iterable может выступать любой итерируемый объект:
# 1. список;
# 2. кортеж;
# 3. строка;
# 4. множество;
# 5. словарь и т.д.

print(all([True, True, True]))  # возвращает True, так как все значения списка равны True
print(all([True, True, False]))  # возвращает False, так как не все значения списка равны True
# True
# False

# ------------
# В Python все следующие значения приводятся к значению False:
# 1. константы None и False;
# 2. нули всех числовых типов данных: 0, 0.0, 0j, Decimal(0), Fraction(0, 1);
# 3. пустые коллекции: '', (), [], {}, set(), range(0).

print(all([1, 2, 3]))
print(all([1, 2, 3, 0, 5]))
print(all([True, 0, 1]))
print(all(('', 'red', 'green')))
print(all({0j, 3 + 4j}))
# True
# False
# False
# False
# False

# ------------
# При работе со словарями функция all() проверяет на соответствие параметрам True ключи словаря, а не их значения.
dict1 = {0: 'Zero', 1: 'One', 2: 'Two'}
dict2 = {'Zero': 0, 'One': 1, 'Two': 2}

print(all(dict1))
print(all(dict2))
# False
# True

# ------------
# Если переданный итерируемый объект пустой, то функция all() возвращает значение True.

print(all([]))  # передаем пустой список
print(all(()))  # передаем пустой кортеж
print(all(''))  # передаем пустую строку
print(all([[], []]))  # передаем список, содержащий пустые списки
# True
# True
# True
# False


# -------------------------------
# Функция any():

# Встроенная функция any() возвращает значение True, если хотя бы один элемент переданной ей последовательности
# (итерируемого объекта) является истинным (приводится к значению True), и False в противном случае.

# Сигнатура функции следующая: any(iterable). В качестве iterable может выступать любой итерируемый объект:

# 1. список;
# 2. кортеж;
# 3. строка;
# 4. множество;
# 5. словарь и т.д.

print(any([False, True, False]))  # возвращает True, так как есть хотя бы один элемент, равный True
print(any([False, False, False]))  # возвращает False, так как нет элементов, равных True
# True
# False

print(any([0, 0, 0]))
print(any([0, 1, 0]))
print(any([False, 0, 1]))
print(any(['', [], 'green']))
print(any({0j, 3 + 4j, 0.0}))
# False
# True
# True
# True
# True


# ------------
# При работе со словарями функция any() проверяет на соответствие True ключи словаря, а не их значения.

dict1 = {0: 'Zero'}
dict2 = {'Zero': 0, 'One': 1}

print(any(dict1))
print(any(dict2))
# False
# True


# ------------
# Если переданный объект пуст, то функция any() возвращает значение False.

print(any([]))  # передаем пустой список
print(any(()))  # передаем пустой кортеж
print(any(''))  # передаем пустую строку
print(any([[], []]))  # передаем список, содержащий пустые списки
# False
# False
# False
# False

# -------------------------------
# Функции all() и any() в связке с функцией map():


# Приведенный ниже код, проверяет, все ли элементы списка numbers больше 10:
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

result = all(map(lambda x: True if x > 10 else False, numbers))
if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')

# Хотя бы одно число меньше или равно 10

# ------------
# Приведенный ниже код, проверяет, что хотя бы один элемент списка четное число:
numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]

result = any(map(lambda x: x % 2 == 0, numbers))
if result:
    print('Хотя бы одно число четное')
else:
    print('Все числа нечетные')

# Хотя бы одно число четное


# ---------------------------------------------- Функция enumerate() ---------------------------------------------------
# Встроенная функция enumerate() возвращает кортеж из индекса элемента и самого элемента переданной ей
# последовательности (итерируемого объекта).

# Сигнатура функции следующая: enumerate(iterable, start). В качестве iterable может выступать любой итерируемый объект:
# 1. список;
# 2. кортеж;
# 3. строка;
# 4. множество;
# 5. словарь и т.д.

colors = ['red', 'green', 'blue']

for pair in enumerate(colors):
    print(pair)
# (0, 'red')
# (1, 'green')
# (2, 'blue')


# ------------
# С помощью необязательного параметра start можно задать начальное значение индекса. По умолчанию значение
# параметра start = 0, то есть счет начинается с нуля.

colors = ['red', 'green', 'blue']

for pair in enumerate(colors, 100):
    print(pair)
# (100, 'red')
# (101, 'green')
# (102, 'blue')

# ------------
# ! Функция enumerate() возвращает не список, а итератор.

colors = ['red', 'green', 'blue']
pairs = enumerate(colors)

print(pairs)
print(list(pairs))
# <enumerate object at 0x000001E5920E4950>
# [(0, 'red'), (1, 'green'), (2, 'blue')]

colors = ['red', 'green', 'blue']
for index, item in enumerate(colors):
    print(index, item)
# 0 red
# 1 green
# 2 blue


# ---------------------------------------------------- Функция zip() ---------------------------------------------------

# Встроенная функция zip() объединяет отдельные элементы из каждой переданной ей последовательности
# (итерируемого объекта) в кортежи.

# Сигнатура функции следующая: zip(*iterables). В качестве iterable может выступать любой итерируемый объект:
# 1. список;
# 2. кортеж;
# 3. строка;
# 4. множество;
# 5. словарь и т.д.

numbers = [1, 2, 3]
words = ['one', 'two', 'three']

for pair in zip(numbers, words):
    print(pair)
# (1, 'one')
# (2, 'two')
# (3, 'three')

# ! Функция zip() возвращает не список, а итератор.

numbers = [1, 2, 3]
words = ['one', 'two', 'three']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
# [(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', 'III')]

# ------------
# Мы можем передать функции zip() даже один итерируемый объект:
numbers = [1, 2, 3]
result = zip(numbers)
print(list(result))
# [(1,), (2,), (3,)]

# ------------
# Если функции zip() передать итерируемые объекты, имеющие разную длину, то объект с наименьшим количеством элементов
# определяет итоговую длину.

numbers = [1, 2, 3, 4]
words = ['one', 'two']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
# [(1, 'one', 'I'), (2, 'two', 'II')]


# -------------------------------
# Частые сценарии использования функции zip():

# Сценарий 1. Функция zip() удобна для создания словарей, когда ключи и значения находятся в разных списках.
keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info)
# {'name': 'Timur', 'age': 28, 'gender': 'male'}


# Сценарий 2. Функция zip() удобна для одновременного (параллельного) итерирования сразу по нескольким коллекциям.
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]

for x, y in zip(name, age):
    print(x, y)
# Timur 28
# Ruslan 21
# Rustam 19

# ------------
# Мы можем использовать одновременно функции zip() и enumerate():
list1 = ['a1', 'a2', 'a3']
list2 = ['b1', 'b2', 'b3']

for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(index, item1, item2)


# 0 a1 b1
# 1 a2 b2
# 2 a3 b3


# -------------------------------
# Задачи:

def ignore_command(command):
    """Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
    и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет."""
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    return any(map(lambda x: x in command, ignore))


if __name__ == '__main__':
    print(ignore_command('get ip'))
    print(ignore_command('select all'))
    print(ignore_command('delete'))
    print(ignore_command('trancate'))
# True
# True
# True
# False


# ------------

from typing import Any


def parallel_iteration(*args: Any) -> None:
    """Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о
    стране в формате:
    <capital> is the capital of <country>, population equal <population> people."""

    for cnt, cpt, ppl in zip(*args):
        print(f"{cpt} is the capital of {cnt}, population equal {ppl} people.")


if __name__ == '__main__':
    countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
    capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
    population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

    parallel_iteration(countries, capitals, population)


# ------------

from math import pow


def inside_the_ball(*args: tuple) -> bool:
    """На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y)
    и аппликат (z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с
    введенными координатами внутри либо на поверхности шара с центром в начале координат и радиусом R=2."""

    all_coords = [list(map(float, [x, y, z])) for x, y, z in zip(*args)]
    all_coords = [list(map(lambda x: pow(x, 2), i)) for i in all_coords]

    return all(map(lambda s_crds: s_crds <= 4., map(sum, all_coords)))


if __name__ == '__main__':
    abscissas, ordinates, applicates = [input().split() for _ in range(3)]
    print(inside_the_ball(abscissas, ordinates, applicates))


# ------------

def check_correct_ip_address(ip=None, error=False) -> bool:
    """IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP.
    В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел
    (октетов) со значением от 0 до 255 (включительно), разделённых точками, например, 192.168.1.2.

    Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты
    в IP-адресе – числа со значением от 0 до 255."""

    if ip is not None:
        return all(list(map(lambda x: x in range(0, 255 + 1), ip)))
    else:
        return error


if __name__ == '__main__':
    try:
        input_address_users = list(map(int, input().split(".")))
    except ValueError as e:
        print(check_correct_ip_address())
    else:
        print(check_correct_ip_address(input_address_users))

# ------------

print(["YES", "NO"][any((len(p := input()) < 7, p.isdigit(), p.isalpha(), p.islower(), p.isupper()))])
"""Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную 
и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль."""

# ------------

