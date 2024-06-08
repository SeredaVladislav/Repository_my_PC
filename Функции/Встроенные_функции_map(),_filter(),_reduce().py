# ----------------------------------------- Встроенные функции map(), filter(), reduce() -------------------------------
# -------------------------------
# Встроенная функция map():
# Встроенная функция map() имеет сигнатуру map(func, *iterables)

def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers)  # используем встроенную функцию map()

# Возвращает итератор:
print(new_numbers)  # <map object at 0x00000218DE538070>

for num in new_numbers:  # итерируем циклом for
    print(num)


# 8
# 9
# 10
# 11
# 12
# 13


# ------------
# Приведенный ниже код суммирует элементы трех списков:

def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
numbers3 = [100, 200, 300, 400, 500]

new_numbers = list(map(func, numbers1, numbers2, numbers3))  # преобразуем итератор в список

print(new_numbers)  # [111, 222, 333, 444, 555]


# Если в последовательностях разное количество элементов, то последовательность с минимальным количеством элементов
# становится ограничителем:

def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3


numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20]
numbers3 = [100, 200, 300, 400, 500]

new_numbers = list(map(func, numbers1, numbers2, numbers3))  # преобразуем итератор в список

print(new_numbers)  # [111, 222]

# ------------
# Пример округления:
circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]

result1 = list(map(round, circle_areas, [1] * 6))  # округляем числа до 1 знака после запятой
result2 = list(map(round, circle_areas, range(1, 7)))  # округляем числа до 1,2,...,6 знаков после запятой

print(circle_areas)  # [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
print(result1)  # [3.6, 5.6, 4.3, 6.2, 91.0, 32.0]
print(result2)  # [3.6, 5.58, 4.319, 6.2024, 91.01344, 32.01213]


# -------------------------------
# Встроенная функция filter():
# Встроенная функция filter() имеет сигнатуру filter(func, iterable)


# Удаляем все отрицательные значения из массива:
def func(elem):
    return elem >= 0


numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  # преобразуем итератор в список

print(positive_numbers)  # [2, 4, 0, 10]


# Проверяет, являются ли элементы в последовательности True.
# В первый аргумент передается значение None, во второе - массив значений:
true_values = filter(None, [1, 0, 10, '', None, [], [1, 2, 3], ()])

for value in true_values:
    print(value)
# 1
# 10
# [1, 2, 3]


# ------------
# !
# Если нам нужны строковые методы в виде функций, мы можем получить их через название типа str.
pets = ['alfred', 'tabitha', 'william', 'arla']
chars = ['x', 'y', '2', '3', 'a']

uppered_pets = list(map(str.upper, pets))
capitalized_pets = list(map(str.capitalize, pets))
only_letters = list(filter(str.isalpha, chars))

print(uppered_pets)
print(capitalized_pets)
print(only_letters)

# -------------------------------
# Функция reduce():
# Функция reduce() имеет сигнатуру reduce(func, iterable, initializer=None). Если начальное значение не установлено,
# то в его качестве используется первое значение из последовательности iterable.

from functools import reduce


def func(a, b):
    return a + b


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(func, numbers, 0)  # в качестве начального значения 0
print(total)  # 55
total = reduce(func, numbers)  # в качестве начального значения первый элемент списка numbers

# ---------------------------------------------------- Модуль operator -------------------------------------------------
# Импортирует основные функции математических операций из модуля.
# Реализованы на С.


# Операция	Синтаксис	Функция
# Addition	a + b	add(a, b)
# Containment Test	obj in seq	contains(seq, obj)
# Division	a / b	truediv(a, b)
# Division	a // b	floordiv(a, b)
# Exponentiation	a ** b	pow(a, b)
# Modulo	a % b	mod(a, b)
# Multiplication	a * b	mul(a, b)
# Negation (Arithmetic)	-a	neg(a)
# Subtraction	a - b	sub(a, b)
# Ordering	a < b	lt(a, b)
# Ordering	a <= b	le(a, b)
# Equality	a == b	eq(a, b)
# Difference	a != b	ne(a, b)
# Ordering	a >= b	ge(a, b)
# Ordering	a > b	gt(a, b)

from operator import *  # импортируем все функции

print(add(10, 20))  # сумма
print(floordiv(20, 3))  # целочисленное деление
print(neg(9))  # смена знака
print(lt(2, 3))  # проверка на неравенство <
print(lt(10, 8))  # проверка на неравенство <
print(eq(5, 5))  # проверка на равенство ==
print(eq(5, 9))  # проверка на равенство ==

# 30
# 6
# -9
# True
# False
# True
# False


from functools import reduce
import operator

words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

opposite_numbers = list(map(operator.neg, numbers))  # смена знаков элементов списка
concat_words = reduce(operator.add, words)  # конкатенация элементов списка

print(opposite_numbers)  # [-1, -2, 6, 4, -3, -9, 0, 6, 1]
print(concat_words)  # Testing shows the presence, not the absence of bugs



