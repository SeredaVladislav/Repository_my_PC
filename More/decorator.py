# ---------------------------------------------- Декораторы ------------------------------------------------------------
def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, которые будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper


@my_decorator
def my_function():
    print("Я - оборачиваемая функция!")
    return 0


print(my_function())
# ----------------------------------------------------------------------------------------------------------------------
import time


def decorator_time(fn):
    def wrapper():
        print(f"Запустилась функция {fn}")
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы

    return wrapper


def pow_2():
    return 10000000 ** 2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458

# ----------------------------------------------------------------------------------------------------------------------
import time

N = 100


def decorator_time(fn):
    def wrapper():
        t0 = time.perf_counter_ns()
        result = fn()
        dt = time.perf_counter_ns() - t0
        return dt

    return wrapper


def pow_2():
    return 10000000 ** 2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")


# ----------------------------------------------------------------------------------------------------------------------

def my_decor(func):  # функция
    def wrapper():  # вложенная функция
        print("Начало")  # вывод значения вложенной функции
        func()  # значение-аргумент первой функции во вложенной
        print("Конец")  # вывод значения-аргумента первой функции

    return wrapper  # возвращение значения вложенной функции


def my_func():  # основная функция
    print("Основная функция")  # вывод значение основной функции


test = my_decor(my_func)  # переменная-функция
test()  # вызов результата переменной-функции номер 1


# ----------------------------------------------------------------------------------------------------------------------
#  2 способ декорирования

def my_decor(func):  # функция
    def wrapper():  # вложенная функция
        print("Начало")  # вывод значения вложенной функции
        func()  # значение-аргумент первой функции во вложенной
        print("Конец")  # вывод значения-аргумента первой функции

    return wrapper  # возвращение значения вложенной функции


@my_decor  # декоратор первой функции
def my_func():  # основная функция
    print("Основная функция")  # вывод значение основной функции


my_func()


# ----------------------------------------------------------------------------------------------------------------------

#  2 способ декорирования (со значением)

def my_decor(func):
    def wrapper(a):  # указание аргумента (a) во вложенной функции
        print("Начало")
        func(a)  # вызов аргумента основной функции с аргументом вложенной функции
        print("Конец")

    return wrapper


@my_decor  # декоратор 1 функции
def my_func(number):
    print(number ** 5)


my_func(10)


# ----------------------------------------------------------------------------------------------------------------------

def do_operation(a, b, operation):  # Функция 1
    result = operation(a, b)  # присваиваем 3 аргумент в качестве функции, с 2 первыми аргументами основной функции
    print(f'результат: {result}')  # печать переменной функции 1


def sum(c, d):  # Функция 2
    return c + d  # возврат вычисления функции 2


def mult(e, f):  # Функция 3
    return e * f  # возврат вычисления функции 3


do_operation(5, 4, sum)  # вызов функции 2 с аргументами, через функцию 1 с функцией 2 в качестве аргумента
do_operation(5, 6, mult)  # вызов функции 3 с аргументами, через функцию 1 с функцией 3 в качестве аргумента


# ---------------------------------------------- «Синтаксический сахар» ------------------------------------------------

def my_decorator(fn):
    def wrapper():
        fn()

    return wrapper  # возвращается задекорированная функция, которая заменяет исходную


# выведем не задекорированную функцию
def my_function():
    pass


print(my_function)  # <function my_function at 0x7f938401ba60>


# выведем задекорированную функцию
@my_decorator
def my_function():
    pass


print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>


# ----------------------------------------------------------------------------------------------------------------------
def do_it_twice(func):
    def wrapper(a):
        func(a)

    return wrapper


@do_it_twice
def say_word(word):
    print(word)


say_word("Oo!!!")


# ----------------------------------------------------------------------------------------------------------------------

# декоратор, в котором встроенная функция умеет принимать аргументы
def do_it_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_it_twice
def say_word(word):
    print(word)


say_word("Oo!!!")


# ----------------------------------------------------------------------------------------------------------------------
# Универсальный декоратор
def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result

    return wrapper


# ----------------------------------------------------------------------------------------------------------------------

def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f"Функция {func} была вызвана {count} раз")

    return wrapper


@counter
def say_word(word):
    print(word)


say_word("Oo!!!")
# Функция была вызвана 1 раз

say_word("Oo!!!")


# Функция была вызвана 2 раз
# ----------------------------------------------------------------------------------------------------------------------

def cache(func):
    cache_dict = {}

    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f"Добавление результата в кэш: {cache_dict[num]}")
        else:
            print(f"Возвращение результата из кэша: {cache_dict[num]}")
        print(f"Кэш {cache_dict}")
        return cache_dict[num]

    return wrapper


# ----------------------------------------------------------------------------------------------------------------------

from time import time, sleep  # импорт функции времени и задержки


def my_timer(func):  # функция таймер - декоратор
    def wrapper():
        start_time = time()  # запуск времени
        func()
        end_time = time()  # завершение времени
        print(f'Время работы функции - {end_time - start_time}, c.')  # вывод результата

    return wrapper


@my_timer  # задекорированная функция
def my_func():
    sleep(3)  # задержка 3 сек


my_func()
# ----------------------------------------------------------------------------------------------------------------------

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)


def is_auth(func):
    def wrapper():
        if yesno == 'Y':
            print("Пользователь авторизован")
            func()
        elif yesno == 'N':
            print("Отмена входа")
        else:
            print("Пользователь не авторизован.")

    return wrapper


def has_access(log):
    def wrapper():
        username = input("Введите ваш username: ")
        if username in USERS:
            log()
        else:
            print("Неверный логин")

    return wrapper


@is_auth
@has_access
def from_db():
    print("Добро пожаловать в базу данных!")


from_db()


# ----------------------------------------------------------------------------------------------------------------------

def my_dec(a):
    def wrapper():
        print("Hello!")
        a()

    return wrapper


@my_dec
def my_func2():
    print("World")


my_func2()
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------- Передача функции в качестве аргумента ------------------------------------------
def say_hello(name):  # функция 1
    return f"Привет, {name}!"  # возврат строки с переменной аргументом


def be_awesome(name):  # функция 2
    return f"Класс, {name}, быть вместе так круто!"  # возврат строки с переменной аргументом


def greet_vanya(greeter_func):  # функция 3
    return greeter_func("Ваня")  # возврат аргумента функции!


print(greet_vanya)  # <function greet_vanya at 0x000001A4471E9EE0> если просто вызвать функцию 3 без передачи аргумента
print(greet_vanya(be_awesome))  # передача функции 2 в качестве аргумента к функции 3


# --------------------------------------------- Внутренние функции -----------------------------------------------------
def parent():  # родительская функция
    print("Привет из функции parent().")

    def first_child():  # внутренняя функция 1
        print("Привет из функции first_child().")

    def second_child():  # внутренняя функция 2
        print("Привет из функции second_child().")

    second_child()  # порядок определения не имеет значения (печать только при вызове функции внутри)
    first_child()  #


parent()  # вызов родительской функции


# --------------------------------------------- Возврат функций из функций ---------------------------------------------

def parent(num):  # родительская функция
    def first_child():  # внутренняя функция 1
        return "Привет, меня зовут Ксавье."

    def second_child():  # внутренняя функция 2
        return "Зови меня X Æ A-12."

    if num == 1:  # условие для возврата
        return first_child  # возврат функции 1
    else:
        return second_child  # возврат функции 2


first = parent(1)  # присвоение переменной, по условию, функции 1
second = parent(2)  # присвоение переменной, по условию, функции 1

print(first)  # ссылка на функцию 1
print(second)  # ссылка на функцию 1

print(first())  # вызов внутренней функции 1
print(second())  # вызов внутренней функции 2


# в итоге мы получили доступ во внутренние функции материнской def parent(digit)

# --------------------------------------------- Простые декораторы -----------------------------------------------------

def decorator(func):
    def wrapper():
        result = func()
        ans = ""
        # ans += "-" * (len(result) + 2)
        ans += f"|{result}|"
        # ans += "-" * (len(result) + 2)
        return ans

    return wrapper


@decorator
def get_hello():
    return "Hello!"


print(get_hello())


def my_decorator(func):  # родительская функция
    def wrapper():  # внутренняя функция
        print("До вызова функции.")
        func()  # ссылка на функцию 2
        print("После вызова функции.")

    return wrapper  # возврат функции wrapper в родительскую функцию


def say_whee():  # функция 2
    print("Ура!")


say = my_decorator(say_whee)  # присвоение в переменную родительской функции (декорирование)
print(say)  # ссылка на внутреннюю функцию wrapper()
say()  # вывод декоратора

from datetime import datetime


def not_during_the_night(func):  # родительская функция
    def wrapper():  # внутренняя функция
        if 8 <= datetime.now().hour < 22:  # условие
            func()  # ссылка на функцию 2
        else:
            print("Не кричи! Уже поздно")

    return wrapper  # возврат функции wrapper в родительскую функцию


def say_whee():  # функция 2
    print("Ура!")


say = not_during_the_night(say_whee)  # присвоение в переменную родительской функции (декорирование)

say()  # вывод декоратора


# --------------------------------------------- Немного синтаксического сахара! ----------------------------------------

def my_decorator(func):
    def wrapper():
        print("До вызова функции.")
        func()
        print("После вызова функции.")

    return wrapper


@my_decorator  # синтаксический сахар в декорировании (вместо: say_whee = my_decorator(say_whee))
def say_whee():
    print("Ура!")


say_whee()


# ----------------------------------------- Повторное использование декораторов ----------------------------------------

# создаем новый файл.py (с именем: decorators.py) и пишем в нем код:
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


# далее в другом файле.py:
from decorators import do_twice  # из файла decorators.py импортируем декоратор с помощью @do_twice


@do_twice  # декорируем функцию
def say_whee():
    print("Ура!")


say_whee()  # вызываем задекорированную функцию


# ----------------------------------------- Декорирование функций, принимающих аргументы -------------------------------

# создаем новый файл.py (с именем: decorators.py) и пишем в нем код:
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):  # для декорации функции со своим аргументом, указать в декораторе аргументы
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


# далее в другом файле.py:
from decorators import do_twice  # из файла decorators.py импортируем декоратор с помощью @do_twice


@do_twice  # декорируем функцию со своим аргументом
def greet(name):
    print(f"Привет, {name}")


greet("Мир")


def dec(h):
    def wrapper(m):
        if isinstance(m, int):
            return h(m)
        else:
            return list(map(h, list_))

    return wrapper


@dec
def dfg(a):
    return a ** 2


list_ = [1, 2, 3, 4, 5]

print(dfg(list_))
print(dfg(12))
