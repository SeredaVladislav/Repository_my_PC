# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ tuple (Кортежи) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Не изменяемый;
# Хэшируемый;
# Последовательный;
# Итерируемый.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Создание кортежа:
example = ()
print(example)  # ()

example_2 = tuple()
print(example_2)  # ()

example_3 = 105,
print(example_3)  # (105,)

example_4 = 1, 'a', 3, 'b'
print(example_4)  # (1, 'a', 3, 'b')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Примеры кортежей:
empty_tuple = ()  # пустой кортеж
point = (1.5, 6.0)  # кортеж из двух чисел
names = ('Timur', 'Ruslan', 'Roman')  # кортеж из трех строк
info = ('Timur', 'Guev', 28, 170, 60, False)  # кортеж из 6 элементов разных типов
nested_tuple = (('one', 'two'), ['three', 'four'])  # кортеж из кортежа и списка

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразование строки str в кортеж:
example_5 = tuple('abc')
print(example_5)  # ('a',' b',' c')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразование списка list в кортеж:
example_6 = tuple([1, 2, 3])
print(example_6)  # (1, 2, 3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразование множества set в кортеж:
example_7 = tuple({1, 2, 3})
print(example_7)  # (1, 2, 3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразование генератора в кортеж:
example_8 = tuple(range(5))
print(example_8)  # (0, 1, 2, 3, 4)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразование кортежа в строку:
notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
string1 = ''.join(notes)
string2 = '.'.join(notes)

print(string1)  # DoReMiFaSolLaSi
print(string2)  # Do.Re.Mi.Fa.Sol.La.Si

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразование int в кортеж невозможен, т.к. int не является итерируемым объектом:
number = 12345
tpl = tuple(number)
print(tpl)  # TypeError: 'int' object is not iterable

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Преобразования. Примеры:
str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)
print(str_tuple)  # ('один', 'два', 'три')

text = 'hello python'
str_tuple = tuple(text)
print(str_tuple)  # ('h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n')

writer = ('Лев Толстой', 1827)
print(writer)  # ('Лев Толстой', 1827)

a = list(writer)
a[1] = 1828
writer = tuple(a)
print(writer)  # ('Лев Толстой', 1828)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Кортежи поддерживают:

# доступ к элементу по индексу (только для получения значений элементов);
# методы, в частности index(), count();
# встроенные функции, в частности len(), sum(), min() и max();
# срезы;
# оператор принадлежности in;
# операторы конкатенации (+) и повторения (*).


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Кортежи не поддерживают такие методы:
# append(), remove(), pop(), insert(), reverse(), sort(), так как эти методы изменяют содержимое.


# Добавление в новый список кортежей, которые не являются пустыми:
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i is not tuple()]

print(non_empty_tuples)  # [('',), ('a', 'b'), ('a', 'b', 'c'), (1,), ('d',), ('', '')]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Создание нового списка с последним измененным элементом кортежа:
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []

for i in range(len(tuples)):
    app = list(tuples[i])
    app[-1] = 100
    new_tuples.append(tuple(app))

print(new_tuples)

# 2-й вариант:
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []

for el in tuples:
    new_tuples.append(el[1:] + (100,))

print(new_tuples)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Кортежи можно сравнивать между собой.

print((1, 8) == (1, 8))  # True
print((1, 8) != (1, 10))  # True
print((1, 9) < (1, 2))  # False
print((2, 5) < (6,))  # True
print(('a', 'bc') > ('a', 'de'))  # False

# Операции == и != применимы к любым кортежам, независимо от типов элементов.
# Операции <, >, <=, >= применимы только в том случае, когда соответствующие элементы кортежей имеют один тип.

print((7, 5) < ('java', 'python'))
# TypeError: '<' not supported between instances of 'int' and 'str'

# Сравнение кортежей происходит последовательно элемент за элементом, а если элементы равны
# — просматривается следующий элемент.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Сортировка кортежей:

not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)  # (34, 1, 8, 67, 5, 9, 0, 23)

sorted_tuple = tuple(sorted(not_sorted_tuple))
print(sorted_tuple)  # (0, 1, 5, 8, 9, 23, 34, 67)

# Функция sorted() возвращает список, но с помощью функции tuple() приводим результат сортировки к кортежу.
# Для сортировки кортежа можно воспользоваться явным преобразованием в список и использовать метод sort():

not_sorted_tuple = ('cc', 'aa', 'dd', 'bb')
tmp = list(not_sorted_tuple)
tmp.sort()

sorted_tuple = tuple(tmp)
print(sorted_tuple)  # ('aa', 'bb', 'cc', 'dd')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задачи:
from math import pow


def vertex_of_parabola() -> tuple:
    """Уравнение параболы имеет вид y == a(x**2) + bx + c, где a != 0.
    Напишите программу, которая по введенным значениям a, b, c
    определяет и выводит вершину параболы."""

    a, b, c = [int(input()) for _ in range(3)]

    coords: float = -b / (2 * a)
    coords2: float = (4 * a * c - pow(b, 2)) / (4 * a)

    return coords, coords2


if __name__ == '__main__':
    print(vertex_of_parabola())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def competitive_selection():
    """Формат входных данных:
        На вход программе подается натуральное число n, далее следует
        n строк с фамилией школьника и его оценкой на каждой из них.
        Формат выходных данных:
        Программа должна вывести сначала все введённые строки с фамилиями и
        оценками учеников в том же порядке. Затем следует пустая строка, а
        затем выводятся строки с фамилиями и оценками хорошистов и
        отличников (в том же порядке)."""

    number_of_students: int = int(input())

    list_students: list = [input().split() for _ in range(number_of_students)]

    for all_name in list_students:
        print(" ".join(all_name))

    print()

    for best_name in list_students:
        if int(best_name[-1]) > 3:
            print(" ".join(best_name))


if __name__ == '__main__':
    competitive_selection()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Распаковка кортежей:

colors = ('red', 'green', 'blue', 'cyan')
a, b, c, d = colors
print(a)  # red
print(b)  # green
print(c)  # blue
print(d)  # cyan
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

colors2 = ('red', 'green', 'blue', 'cyan')
a1, b1 = colors2  # ValueError: too many values to unpack
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Распаковка только 2-х первых элементов:
colors3 = ('red', 'green', 'blue')
a2, b2, _ = colors3
print(a2)
print(b2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Распаковка в последнюю переменную остаток значений:
a3, b3, *tail = 1, 2, 3
print(tail)  # [3]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Распаковка в первую переменную всех значений кроме последнего:
*names, surname = ('Стефани', 'Джоанн', 'Анджелина', 'Джерманотта')
print(names)  # ['Стефани', 'Джоанн', 'Анджелина']
print(surname)  # Джерманотта
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

singer = ('Freddie', 'Bohemian Rhapsody', 'Killer Queen', 'Love of my life', 'Mercury')
name, *songs, surname = singer
print(name)  # Freddie
print(songs)  # ['Bohemian Rhapsody', 'Killer Queen', 'Love of my life']
print(surname)  # Mercury
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a4 = 1,      # не распаковка, а просто присвоение
b4, = 1,     # распаковка

print(a4)  # (1,)
print(b4)  # 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Распаковка списка строк:
info = ['timur', 'beegeek.org']
user, domain = info    # распаковка списка
print(user)  # timur
print(domain)  # beegeek.org

# Распаковка строки по-элементно:
a, b, c, d = 'math'    # распаковка строки
print(a)  # m
print(b)  # a
print(c)  # t
print(d)  # h
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Последовательность Фибоначчи:
n = int(input())
f1, f2 = 1, 1
for i in range(n):
    print(f1)
    f1, f2 = f2, f1 + f2


# Последовательность Трибоначчи:
n = int(input())
f1, f2, f3 = 1, 1, 0
for i in range(n):
    print(f1, end=" ")
    f1, f2, f3 = f2, f2 + f3, f2 + f1
