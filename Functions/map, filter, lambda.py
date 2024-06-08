# ---------------------------------------------- map -------------------------------------------------------------------

# Псевдокод
def map_(func, some_list):
    # some_list объект, над которым будет производиться преобразование
    # func функция, которая должна выполняться над каждым объектом
    outp = []
    for i in range(len(some_list)):
        outp.append(func(some_list[i]))
    return outp


map(function, iter1, iter2, ...)  # вместо функции выше

print(list(map(pow_, a_list)))  # [1, 4, 9]

for i in map(pow_, a_list):
    pass

L = ['THIS', 'IS', 'LOWER', 'STRING']

h = list(map(str.lower, L))  # перевод списка в нижний регистр

print(type(h))


# ---------------------------------------------- filter ----------------------------------------------------------------
# Псевдокод
def filter(func, cont):
    outp = []
    for x in cont:  # проходим циклом по итерируемому объекту
        if func(x):  # проверяем условие для каждого элемента
            outp.append(x)  # если True, добавляем в новый список
    return outp


# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))  # [1, 2]


# Из заданного списка вывести только положительные элементы
def positive(x):
    return x % 2 == 0  # функция возвращает четные числа


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))  # [1, 2]

# map + filter
some_list = [i - 10 for i in range(20)]


def pow2(x):
    return x ** 2


def positive(x):
    return x > 0


print(list(map(pow2, filter(positive, some_list))))

g = [i ** 2 for i in some_list if i > 0]  # то же самое через генератор списка
print(g)

# ---------------------------------------------- Lambda функции --------------------------------------------------------


data = {
    82: 1.91,
    68: 1.74,
    90: 1.89,
    73: 1.79,
    76: 1.84
}

for key, value in data.items():
    print(key / (value ** 2))

# (вес, рост)
data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]

f = sorted(data, key=lambda x: x[0] / x[1] ** 2)

print(f)

data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]

value_ = min(data, key=lambda x: x[0] / x[1] ** 2)  # нахождение минимального выражения через min()

print(value_)

a = [2, 8, 5, 9, 4, 11, 2, 4]

print(min(a, key=lambda x: x % 5))  # нахождение минимального выражения через min() с условием row % 5
# 5


points = [
    (1, 4),
    (2, 10),
    (1, 1),
    (1, 5)
]

print(min(points, key=lambda x: x[0] + x[1]))  # нахождение близкой к нулю точки

points = [
    (1, 4, 2),
    (2, 10, 6),
    (1, 1, 7),
    (1, 5, 4)
]

points.sort(key=lambda x: -sum(x))  # поиск периметра треугольник через sorted, с условием суммы всех сторон
print(points)

# функция enumerate перебирает значения и индексы элементов, функция min выводит минимальное значение, функция lambda
# выводит только первый минимальный элемент с сортировкой: индекс - значение

list_ = [1, 2, -5, 1, 6, 8, -11, 5, 20, -6]
min_value_min_index = min(enumerate(list_), key=lambda x: x[1])  # нахождение минимального значения и его индекса
print(min_value_min_index)

list_ = [1, 2, -5, 1, 6, 8, -11, 5, 20, -6]
min_value_min_index = min(enumerate(list_), key=lambda x: x[1])[0]  # вывод только минимального индекса элемента
print(min_value_min_index)

list_ = [1, 2, -5, 1, 6, 8, -11, 5, 20, -6]
min_value_min_index = min(enumerate(list_), key=lambda x: x[1])[1]  # вывод только минимального элемента
print(min_value_min_index)

# Lambda - функции:
# ==================
# Lambda аргументы: выражение
# ==================

# 1.1. Пример лямбда-функции.============================================

double = lambda x: x * 2
print(double(2))  # 10


# Lambda row: row * 2 — это лямбда-функция.
# Здесь row — это аргумент.
# row * 2 — это выражение, которое вычисляется и возвращается

# то же самое, что и:
def double(x):
    return x * 2


# 2. Различие между обычной функцией и лямбда-функцией =================

def defined_cube(y):
    return y * y * y


print(defined_cube(2))  # 8

lambda_cube = lambda y: y * y * y

print(lambda_cube(2))  # 8

# 3. Лямбда-функции и функции высшего порядка ==========================
# 3.1. Пример с filter() ===============================================
# Функция вызывается со всеми элементами в списке, и в результате возвращается новый список, содержащий
# элементы, для которых функция результирует в True

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))  # list(filter(lambda row: функция, итерируемый объект)
print(new_list)  # [4, 6, 10, 12, 14]

# 3.2. Пример с map() =================================================
# Функция вызывается со всеми элементами в списке, и в результате возвращается новый список, содержащий
# элементы, возвращенные данной функцией для каждого исходного элемента.


current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x * 2, current_list))  # list(map(lambda row: функция, итерируемый объект)
print(new_list)

# 3.3. Пример с reduce() ===============================================
# Функция reduce() принимает в качестве аргументов функцию и список.
# Выполняется операции функции с парами из списка поочередно.

from functools import reduce

current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce((lambda x, y: x + y), current_list)  # 5+15+20+30+50+55+75+60+70
print(summa)  # 380

# 4. Лямбда и  списковое включение ======================================

tables = [lambda x=x: x * 10 for x in range(1, 11)]

for table in tables:
    print(table())

# 6. Лямбда и множественные операторы ==================================

current_list = [[10, 6, 9], [0, 14, 16, 80], [8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y) - 2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)

