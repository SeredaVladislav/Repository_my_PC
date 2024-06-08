# ------------------------------------------- Логические операторы -----------------------------------------------------

a = None  # пустая строка
b = a or 1
print(b)  # 1

some_var = None
if some_var is None:  # если some_var Ничего, то вывод NoneType
    print("NoneType")
else:
    print(type(some_var))

# and: если все операнды являются истинными (ненулевые или непустые), то возвращается последнее истинное значение.
print(1 and "hello" and [False])
# [False]


# and: если один из операндов является ложным, то возвращается первый такой операнд.
print(42 and 0 and '' and False)
# 0


# or: если один из операндов является истинным, то возвращается первый такой операнд, а остальные игнорируются.
print([] or 3.14 or False)
# 3.14


# or: если все операнды являются ложными, то возвращается последний.
print(0 or '' or False)
# False


if a is None:  # если a == None, то возвращается b = 1, иначе b = a
    b = 1
else:
    b = a

b = a if a is not None else 1  # этот же случай, но запись через тернарный оператор

b = a or 1  # тот же случай, но короче

a = "foo"
b = "bar"

print(1 and a or b)
#  foo


a = ""
b = "bar"

print(1 and a or b)
#  bar


a = 2
b = 1

if a and b is not None:
    print("Обе переменные истинные")
else:
    print(a, b)

a = 1
b = None

if a and b:
    print("Обе переменные истинные")
else:
    print(a, b)

a = 1
b = None

if a and b:
    print("Обе переменные истинные")
    print(a, b)
elif a or b:
    print("Одна из переменных истинная")
    print(a or b)

a = None
b = None

if a and b:
    print("Обе переменные истинные")
    print(a, b)
elif a or b:
    print("Одна из переменных ложная")
    print(a or b)
else:
    print("Обе переменные ложные")
    print(a and b)

a = int(input(""))

if 100 <= a <= 999:
    if a % 1 == 0:
        if a % 3 == 0 and a % 2 == 0:
            print("Число соответствует!")
        else:
            print("Число не подходит")
    else:
        print("Число не подходит")
else:
    print("Число не подходит")

if type(a) == int:
    if 100 <= a <= 999:
        if a % 2 == 0:
            if a % 3 == 0:
                print("Число удовлетворяет условиям")

if 100 <= a <= 999 and a % 1 == 0 and a % 2 == 0 and a % 3 == 0:
    print("Число удовлетворяет условиям")
else:
    print("Число не подходит")

# Функция all([ ]) возвращает True, если все элементы списка являются истинными.
# А что если нужно, чтобы был хотя бы один истинный? Тогда на помощь приходит функция any([ ]).
# Ее синтаксис аналогичен рассмотренному выше примеру c функцией all([ ]).


if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")


L = list(map(int, input().split()))

print(all(L))


L = list(map(int, input().split()))

print(not any(L))