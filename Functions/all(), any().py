# Функция all() возвращает значение True, если все элементы в итерируемом объекте - истинны, в противном случае она
# возвращает значение False.

# Если передаваемая последовательность пуста, то функция all() также возвращает True.

def all_func(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print(all([True, True, True]))
# True
print(all([True, False, True]))
# False


# ------------------
# Пример:
num1 = range(1, 9)
num2 = range(-1, 7)
print(all([x > 0 for x in num1]))
# True
print(all([x > 0 for x in num2]))
# False


# ------------------
num1 = [1, 2, 3, 4, 5, 6, 7]
num2 = [1, 2.0, 3.1, 4, 5, 6, 7.9]
print(all([type(x) is int for x in num1]))
# True
print(all([type(x) is int for x in num2]))


# False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Функция any() возвращает True, если какой-либо (любой) элемент в итерируемом объекте является истинным True, в
# противном случае any() возвращает значение False.

# Если последовательность пуста, то функция any() возвращает False.

def any_func(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(False or True or False)
# True
print(any([False, True, False]))
# True


# ------------------
# Пример:
addr1 = '142100, г. Москва, ул. Свердлова, 15'
addr2 = '142100, г. Москва, ул. Свердлова'
print(any(map(str.isdigit, addr1.rsplit(' ', 1))))
# True
print(any(map(str.isdigit, addr2.rsplit(' ', 1))))
# False


# ------------------
num1 = range(0, 20, 2)
num2 = range(0, 15, 2)
print(any([x > 15 for x in num1]))
# True
print(any([x > 15 for x in num2]))
# False
