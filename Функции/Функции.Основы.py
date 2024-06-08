# Необязательные и именованные аргументы.
# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------
# Позиционные аргументы:
def diff(x, y):
    return x - y


res = diff(10, 3)  # используем позиционные аргументы
print(res)


# -------------------------------
# Именованные аргументы:
def diff(x, y):
    return x - y


res = diff(x=10, y=3)  # используем именованные аргументы
print(res)


# -------------------------------
# Когда стоит применять именованные аргументы:
def make_circle(x, y, radius, line_width, fill):
    pass


make_circle(x=200, y=300, radius=17, line_width=2.5, fill=True)

# -------------------------------
# Комбинирование позиционных и именованных аргументов:
res = diff(10, y=3)  # используем позиционный и именованный аргумент.
# ----------------------------------------------------------------------------------------------------------------------
# Необязательные аргументы:
num = int('101', 2)  # аргумент 2 указывает на то, что число 101 записано в двоичной системе.


# -----------------
def make_circle(x, y, radius, line_width=1, fill=True):
    pass


make_circle(100, 50, 20)


# -------------------------------
# Изменяемые типы в качестве значений по умолчанию:
def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq


print(append(10, [1, 2, 3]))
print(append(5, [1]))
print(append(1, []))
print(append(3, [4, 5]))

# Чтобы посмотреть значения по умолчанию, можно использовать атрибут __defaults__:
print('Значение по умолчанию', append.__defaults__)  # Значение по умолчанию ([],)


# ----------------------------------------------------------------------------------------------------------------------
# Функции с переменным количеством аргументов.
# ----------------------------------------------------------------------------------------------------------------------
# Переменное количество аргументов:
# *args = передается неограниченное количество позиционных аргументов в виде кортежа.
def my_func(*args):
    print(type(args))
    print(args)


my_func()
my_func(1, 2, 3)
my_func('a', 'b')


# <class 'tuple'>
# ()
# <class 'tuple'>
# (1, 2, 3)
# <class 'tuple'>
# ('a', 'b')


# -------------------------------
# При комбинированных аргументах, *args ставится в конце всех аргументов.
def my_func(num, *args):
    print(args)
    print(num)


my_func(17, 'Python', 2, 'C#')
# ('Python', 2, 'C#')
# 17


# *args является не обязательным для передачи в него аргументов.
my_func(17)


# ()
# 17


# -------------------------------
# Передача аргументов в форме списка и кортежа:
def my_sum(*args):
    return sum(args)  # args - это кортеж


print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4))
# 0
# 1
# 3
# 6
# 10


# Вызвать функцию передавая ей списки или кортежи, предварительно распаковав их:
print(my_sum(*[1, 2, 3, 4, 5]))  # распаковка списка
print(my_sum(*(1, 2, 3)))  # распаковка кортежа
# 15
# 6


print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10))


# 49


# ----------------------------------------------------------------------------------------------------------------------
# Получение именованных аргументов в виде словаря:
# **kwargs = неопределенное количество именованных аргументов, переданных в виде словаря.
def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)


my_func()
my_func(a=1, b=2)
my_func(name='Timur', job='Teacher')
print()


# <class 'dict'>
# {}
# <class 'dict'>
# {'a': 1, 'b': 2}
# <class 'dict'>
# {'name': 'Timur', 'job': 'Teacher'}

# Параметр  **kwargs пишется в самом конце, после последнего аргумента со значением по умолчанию.
# При этом функция может содержать и *args и **kwargs параметры.
def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)


my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
print()
my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
print()
my_func(1, 2, 3, 4, job='Teacher', language='Python')


# 1 2
# (3, 4)
# Timur 28
# {'job': 'Teacher', 'language': 'Python'}
#
# 1 2
# ()
# Timur 28
# {'job': 'Teacher', 'language': 'Python'}
#
# 1 2
# (3, 4)
# Gvido 17
# {'job': 'Teacher', 'language': 'Python'}


# -----------------
# Передача именованных аргументов в форме словаря:
def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)


info = {'name': 'Timur', 'age': '28', 'job': 'teacher'}

my_func(**info)


# <class 'dict'>
# {'name': 'Timur', 'age': '28', 'job': 'teacher'}


def print_info(name, surname, age, city, *children, **additional_info):
    print('Имя:', name)
    print('Фамилия:', surname)
    print('Возраст:', age)
    print('Город проживания:', city)
    if len(children) > 0:
        print('Дети:', ', '.join(children))
    if len(additional_info) > 0:
        print(additional_info)


children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
additional_info = {'height': 163, 'job': 'actress'}

print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info)


# Имя: Меган
# Фамилия: Фокс
# Возраст: 34
# Город проживания: Ок-Ридж
# Дети: Бодхи Рансом Грин, Ноа Шэннон Грин, Джорни Ривер Грин
# {'height': 163, 'job': 'actress'}


# ----------------------------------------------------------------------------------------------------------------------
# Keyword-only аргументы:
# Здесь * выступает разделителем: отделяет обычные аргументы (их можно указывать по имени и позиционно) от
# строго именованных.


def make_circle(x, y, radius, *, line_width=1, fill=True):
    pass


make_circle(10, 20, 5)  # x=10, y=20, radius=5,  line_width=1, fill=True
make_circle(x=10, y=20, radius=7)  # x=10, y=20, radius=7,  line_width=1, fill=True
make_circle(10, 20, radius=10, line_width=2, fill=False)  # x=10, y=20, radius=10, line_width=2, fill=False
make_circle(x=10, y=20, radius=17, line_width=3)  # x=10, y=20, radius=17, line_width=3, fill=True


# То есть аргументы x, y и radius могут быть переданы в качестве как позиционных, так и именованных аргументов.
# При этом аргументы line_width и fill могут быть переданы только как именованные аргументы.


# -----------------
# Мы также можем объявить функцию, у которой будут только строго именованные аргументы, для этого нужно поставить
# звёздочку в самом начале перечня аргументов.

def make_circle(*, x, y, radius, line_width=1, fill=True):
    pass


make_circle(x=10, y=20, radius=15)  # line_width=1, fill=True
make_circle(x=10, y=20, radius=15, line_width=4, fill=False)


# ----------------------------------------------------------------------------------------------------------------------
# Задачи:

def print_products(*args):
    count = 0

    for i in args:
        if type(i) is str and len(i) != 0:
            count += 1
            print(f"{count}) {i}")

    if count == 0:
        print("Нет продуктов")


if __name__ == '__main__':
    print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# -----------------



