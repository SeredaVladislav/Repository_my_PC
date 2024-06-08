# ---------------------------------------------- Анонимные функции -----------------------------------------------------

# Общий формат определения анонимной функции: lambda список_параметров: выражение.

# Тут список_параметров – список параметров через запятую, выражение – значение, либо код, дающий значение.

# ------------
def standard_function(x):  # стандартное объявление функции
    return x * 2


lambda_function = lambda x: x * 2  # объявление анонимной функции

print(standard_function(7))  # 17
print(lambda_function(7))  # 17

# ------------
f1 = lambda: 10 + 20  # функция без параметров
f2 = lambda х, у: х + у  # функция с двумя параметрами
f3 = lambda х, у, z: х + у + z  # функция с тремя параметрами

print(f1())  # 30
print(f2(5, 10))  # 15
print(f3(5, 10, 30))  # 45


# -------------------------------
# Однократное использование функции:
def compare_by_second(point):  # функция-компаратор
    return point[1]


def compare_by_sum(point):  # функция-компаратор
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))  # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))  # сортируем по сумме кортежа

# Альтернатива с помощью lambda - функции:
points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=lambda point: point[1]))  # сортируем по второму значению кортежа
print(sorted(points, key=lambda point: point[0] + point[1]))  # сортируем по сумме элементов кортежа

# -------------------------------
# Передача анонимных функций в качестве аргументов другим функциям:

numbers = [1, 2, 3, 4, 5, 6]

new_numbers1 = list(map(lambda x: x + 1, numbers))  # увеличиваем на 1
new_numbers2 = list(map(lambda x: x * 2, numbers))  # удваиваем
new_numbers3 = list(map(lambda x: x ** 2, numbers))  # возводим в квадрат

print(new_numbers1)  # [2, 3, 4, 5, 6, 7]
print(new_numbers2)  # [2, 4, 6, 8, 10, 12]
print(new_numbers3)  # [1, 4, 9, 16, 25, 36]

# ------------
strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]

new_strings = list(map(lambda x, y: x * y, strings, numbers))

print(new_strings)  # ['aaa', 'bb', 'c', 'dddd', 'eeeee']

# ------------
numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

positive_numbers = list(filter(lambda x: x > 0, numbers))  # положительные числа
large_numbers = list(filter(lambda x: x > 50, numbers))  # числа, большие 50
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # четные числа

print(positive_numbers)  # [2, 4, 10, 30, 50, 100, 90]
print(large_numbers)  # [100, 90]
print(even_numbers)  # [2, 4, 0, -20, 10, 30, -40, 50, 100, 90]

# ------------
words = ['python', 'stepik', 'beegeek', 'iq-option']

new_words1 = list(filter(lambda w: len(w) > 6, words))  # слова длиною больше 6 символов
new_words2 = list(filter(lambda w: 'e' in w, words))  # слова содержащие букву e

print(new_words1)  # ['beegeek', 'iq-option']
print(new_words2)  # ['stepik', 'beegeek']

# ------------
from functools import reduce

words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa)  # 21
print(product)  # 720
print(sentence)  # Everyone loves python loves stepik loves beegeek loves iq-option


# -------------------------------
# Возвращение функции в качестве результата другой функции:

def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a * x ** 2 + b * x + c

    return square_polynom


# Такой код можно переписать так:
def generator_square_polynom(a, b, c):
    return lambda x: a * x ** 2 + b * x + c  # замыкание lambda - функцией


func2 = generator_square_polynom(2, 4, 6)
print(func2(10))  # 246

# ----------------------------------------- Условный оператор в теле анонимной функции ---------------------------------

numbers = [-2, 0, 1, 2, 17, 4, 5, 6]

result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
print(result)  # ['even', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Общий вид тернарного условного оператора в теле анонимной функции выглядит так:

# значение1 if условие else значение2
# Если условие истинно, возвращается значение1, если нет – значение2.


# ----------------------------------------- Передача аргументов в анонимную функцию ------------------------------------

# Анонимные функции поддерживают все способы передачи аргументов:

# позиционные аргументы;
# именованные аргументы;
# переменный список позиционных аргументов (*args);
# переменный список именованных аргументов (**kwargs);
# обязательные аргументы (*).

f1 = lambda x, y, z: x + y + z
f2 = lambda x, y, z=3: x + y + z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x + y + z

print(f1(1, 2, 3))
print(f2(1, 2))
print(f2(1, y=2))
print(f3(1, 2, 3, 4, 5))
print(f4(one=1, two=2, three=3))
print(f5(1))
print(f5(1, y=2, z=3))

# 6
# 6
# 6
# 15
# 6
# 1
# 6

# ----------------------------------------- Ограничения анонимных функций ----------------------------------------------

# Особенности и ограничения анонимных функций в Python:

# анонимная функция может содержать только выражение, и не может включать в свое тело операторы;
# в теле анонимной функции такие операторы, как return, pass, assert или raise, вызовут исключение SyntaxError;
# анонимная функция пишется как одна строка исполнения;


# анонимная функция может быть немедленно вызвана:
print((lambda х, у: х + у)(5, 10))  # 5 + 10
print(1 + (lambda x: x * 5)(10) + 2)  # 1 + 50 + 2
# 15
# 53


# В Python анонимные функции — лишь сокращенная запись функции, поэтому приведенный ниже код:

f = lambda x: x + 1
print(type(f))
# <class 'function'>

# То есть, анонимные функции имеют такой же тип, как и обычные функции.

# Анонимные функции очень часто используются вместе со встроенными функциями map(),
# filter(), reduce(), sorted(), max(), min() и т.д.


# -------------------------------
# Задачи:
from functools import reduce

"""Требовалось написать программу, которая:
* преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
* фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
* находит произведение чисел из списка numbers."""

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(round, map(lambda x: x ** 2, floats), [1] * (len(floats) + 1)))
filter_result = list(filter(lambda name: name if len(name) > 4 and name == name[::-1] else None, words))
reduce_result = reduce((lambda x, y: x * y), numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)
# [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1, 1171.7, 146.9, 21.8, 6.0, 86.9]
# ['racecar', 'civic', 'TATTARRATTAT', 'malayalam']
# 24840


# ------------
data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

"""Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном 
порядке список primary городов с населением более 10000000 человек, в формате:
Cities: Beijing, Buenos Aires, ..."""

city = list(filter(lambda x: x[2] == 'primary', data))
city = list(filter(lambda x: x if x[1] / 10_000_000 > 1 else None, city))
city = sorted(city, key=lambda x: x[0])
city = [i[0] for i in city]

print("Cities:", ", ".join(city))

# ------------
from operator import mod as m

"""Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает 
значение True, если он делится без остатка на 19 или на 13 и False в противном случае."""

func = lambda x: m(x, 19) == 0 or m(x, 13) == 0

# ------------

func2 = lambda x: str(x).startswith(('a', 'A')) and str(x).endswith(('a', 'A'))

"""Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает 
значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и 
False в противном случае."""

# ------------

is_non_negative_num = lambda x: x.replace('.', '0', 1).isdigit()

"""Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и
 возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным) и False в 
 противном случае."""

# ------------

words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

"""Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words, 
имеющие длину ровно 6 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом 
пробела."""

print(*filter(lambda x: len(x) == 6, sorted(words)))

# ------------
data = [
    (19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
    (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
    (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
    (7029917, 'Massachusetts'), (6910840, 'Tennessee')
]

"""Список data содержит информацию о численности населения некоторых штатов США. Напишите программу сортировки по 
убыванию списка data на основании последнего символа в названии штата. Затем распечатайте элементы этого списка, 
каждый на новой строке в формате:

<название штата>: <численность населения>
Vermont: 626299
Massachusetts: 7029917
..."""

result_data = sorted(data, key=lambda x: x[1][-1], reverse=True)

for i in result_data:
    print(f"{i[-1]}: {i[0]}")

# ------------
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

"""Список data содержит слова на русском языке. Напишите программу, которая сортирует этот список по возрастанию длины 
слов. В случае, если длины каких-то слов совпадают, – отсортировать эти слова в лексикографическом порядке. 
Отсортированные слова следует вывести на одной строке, разделив символом пробела."""

data.sort(key=lambda x: (len(x), x))
print(*data)
# ------------

mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
              'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
              2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
              'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
              859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
              'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
              'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552,
              1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

"""Список mixed_list содержит целочисленные и строковые значения. Напишите программу, которая с помощью встроенной 
функции max() находит и выводит наибольшее числовое значение в указанном списке."""

print(max(list(filter(lambda x: type(x) is int, mixed_list))))

# ------------

mixed_list = [
    'beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
    70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
    13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
    'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
    'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
    'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11
]

"""Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию 
значений элементов, при этом числа должны следовать до строк.  Элементы отсортированного списка выведите на одной 
строке, разделив символом пробела."""

print(*sorted(mixed_list, key=str))

# ------------

rgb = map(int, input().split())

"""В цветовой схеме RGB цвета задаются с помощью трех компонентов:
R — интенсивность красной составляющей цвета;
G — интенсивность зеленой составляющей цвета;
B — интенсивность синей составляющей цвета.
Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). Считается, что такие цвета хорошо гармонируют друг с 
другом.
Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета. """

print(*map(lambda x: abs(x - 255), rgb))

# ------------

coef = list(map(int, input().split()))
x = int(input())

degrees = [i + 1 for i in range(len(coef) - 1)]
print(sum(list(map(lambda z, y: z * y, coef, map(lambda y: x ** y, sorted(degrees, reverse=True))))) + coef[-1])

# ------------

