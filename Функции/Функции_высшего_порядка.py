# ------------------------------------------ Функции высшего порядка ---------------------------------------------------

# Как уже сказано, функции, которые принимают или/и возвращают другие функции, называются функциями высшего порядка.
# Давайте реализуем простейшую функцию высшего порядка:

def high_order_function(func):  # функция высшего порядка, так как принимает функцию
    return func(3)


def double(x):  # обычная функция = функция первого порядка
    return 2 * x


def add_one(x):  # обычная функция = функция первого порядка
    return x + 1


print(high_order_function(double))  # 6
print(high_order_function(add_one))  # 4

# Функции первого порядка принимают и возвращают "обычные" значения, а не функции. Функции же высшего порядка
# принимают и/или возвращают другие функции.


# ------------------------------- Функции высшего порядка для обработки набора данных ----------------------------------
# -------------------------------
# Функция map():

array = [2, 3, 5, 9, 7, 10, 1]

lamb = lambda x: 2 ** x
result_map = map(lamb, array)
print(*result_map)


# Под капотом:
def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result


# -------------------------------
# Цепочки преобразований:

# Вложенные функции map:
numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']

new_numbers = map(abs, map(int, numbers))
print(new_numbers)  # [1, 20, 3, 94, 65, 6, 970, 8]

# Функция map() меняет значение элементов, но не меняет их количество и позиции.


# -------------------------------
# Функция filter():

# Другая популярная задача при работе со списками: отобрать часть элементов списка по определенному критерию.
# Функция высшего порядка для решения такой задачи называется filter().

# Функция-критерий, которая возвращает значение True или False, называется предикатом.

# Под капотом:
def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)  # добавляем элемент item если функция function вернула значение True

    return result


# ------------
numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]


def is_greater10(num):  # функция возвращает значение True если число больше 10 и False в противном случае
    return num > 10


large_numbers = filter(is_greater10, numbers)  # список large_numbers содержит элементы, большие 10
print(large_numbers)  # [12, 48, 51, 19, 13]

# ------------
# Если условие функции вернуло True, то итерируемый элемент возвращается, иначе игнорируется:
gen_numbers = [7, 6, 5, 1, 3, 5, 2]
print(filter(lambda x: x > 3, gen_numbers))  # [7, 6, 5, 5]


# ------------
def is_odd(num):
    return num % 2


def is_word_long(word):
    return len(word) > 6


numbers = list(range(15))
words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']

odd_numbers = filter(is_odd, numbers)
large_words = filter(is_word_long, words)

print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13]
print(large_words)  # ['останутся', 'длинные']

# функция filter() не меняет элементы, а лишь отбрасывает их часть


# -------------------------------
# Функция reduce():

# Необходим импорт:
# from functools import reduce

# Встречаются циклы с агрегацией результата — формированием одного результирующего значения при комбинации элементов
# с использованием аргумента-аккумулятора.

# Типичные примеры агрегации — сумма всех элементов списка или их произведение.

numbers = [1, 2, 3, 4, 5]

total = 0
product = 1

for num in numbers:
    total += num
    product *= num

print(total)  # 15
print(product)  # 120


# Под капотом:
def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc


# ------------

def add(x, y):
    return x+y


def mult(x, y):
    return x*y


numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers, 0)
product = reduce(mult, numbers, 1)

print(total)  # 15
print(product)  # 120


# ------------

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
           11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
           72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
           7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]


b = lambda x, y: x + y ** 2

print(reduce(b, numbers, 0))





