# --------------------------------------------- Обращение к атрибутам класса -------------------------------------------
# -------------------------------
# ------------

# Обращение к атрибутам класса производится по следующей схеме:

# class_name.attribute_name
# где class_name — имя класса, а attribute_name — имя атрибута.

class Person:
    name = 'Jared'
    age = 30


print(Person.name)  # Jared
print(Person.age)  # 30


# -------------------------------
# Функция getattr.
# Функция getattr() возвращает значение именованного атрибута объекта. Если атрибут не найден, функция getattr не
# падает с ошибкой AttributeError, а возвращает значение по умолчанию.

# getattr(object, name, default=None):
# 1. object — это объект, в котором будет осуществлен поиск атрибута;
# 2. name — название атрибута поиска;
# 3. Необязательный аргумент default — значение, получаемое в случае отсутствия искомого атрибута. Если искомого
# атрибута нет в классе и параметр default не задан, происходит обработка исключения AttributeError.

class Person:
    name = 'Jared'
    age = 30


print(getattr(Person, 'name'))  # Jared
print(getattr(Person, 'age'))  # 30


# При отсутствии атрибута:
class Person:
    name = 'Jared'
    age = 30


print(getattr(Person, 'salary', 'Нет такого атрибута'))  # Нет такого атрибута
print(getattr(Person, 'salary', 100))  # 100


# -------------------------------
# Магический атрибут __dict__.
# Возвращает словарь из всех атрибутов класса:

class Person:
    """Класс Person"""
    name = 'Bob'
    age = 35


print(Person.__dict__)  # {'__module__': '__main__', '__doc__': 'Класс Person', 'name': 'Bob', 'age': 35,


# '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}

# -------------------------------
# Функция hasattr.
# hasattr(obj, name) проверяет вхождение конкретного атрибута в классе:
class Person:
    name = 'Jared'
    age = 30


print(hasattr(Person, 'name'))  # True
print(hasattr(Person, 'money'))  # False


# ------------------------------------------ Изменение атрибута класса -------------------------------------------------
# Для изменения значения существующего атрибута класса следует применять следующую конструкцию:
# class_name.attribute_name = value:
# 1. class_name — имя класса;
# 2. attribute_name — имя атрибута;
# 3. value — новое значение атрибута.

class Person:
    name = 'Jared'
    age = 30


print(Person.name)  # Jared
Person.name = 'Michail'
print(Person.name)  # Michail


# ------------------------------------------- Создание атрибута класса -------------------------------------------------
class Person:
    name = 'Ivan'
    age = 30


# При отсутствии атрибута класса, создается новый:
Person.money = 100
Person.phone = '+1 202 777 xxx'
print(Person.money)  # 100
print(Person.phone)  # +1 202 777 xxx


# -------------------------------
# Функция setattr.
# Параметры функции:
# 1. obj: объект, который следует дополнить атрибутом
# 2. name: строка с именем атрибута. Можно указывать как имя нового, так и существующего атрибута.
# 3. value: произвольное значение атрибута.

# Создание нового атрибута через функцию setattr(obj, name, value):
class Person:
    name = 'Ivan'
    age = 30


setattr(Person, 'money', 200)
setattr(Person, 'phone', '+1 202 777 xxx')
print(Person.__dict__)
print()
setattr(Person, 'name', 'Vasya')
setattr(Person, 'age', '43')
print(Person.__dict__)


# -------------------------------
# Удаление атрибутов класса.

# Для удаления атрибута следует применять оператор del или функцию delattr:

# 1. Функция delattr(obj, name):
# obj - из какого объекта;
# name - имя атрибута.

class Person:
    name = 'Ivan'
    age = 30
    money = 200


delattr(Person, 'age')
del Person.money

# Атрибуты age и money были удалены:
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Ivan',


# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# ------------------------------------------- Проверка наличия атрибута ------------------------------------------------
# Функция hasattr() возвращает значение True, если объект имеет заданный именованный атрибут, и значение False,
# если нет.
# hasattr(obj, name):

class Person:
    name = 'Jared'
    age = 30


print(hasattr(Person, 'name'))  # True
print(hasattr(Person, 'salary'))  # False

if hasattr(Person, 'age'):
    print('Атрибут age присутствует')  # Атрибут age присутствует

if not hasattr(Person, 'city'):
    print('Атрибут city отсутствует')  # Атрибут city отсутствует


# ---------------------------------------------------- Задачи ----------------------------------------------------------
# Создание атрибутов класса с помощью функции setattr() из списка кортежей:
class Empty:
    """Имеется пустой класс Empty и список кортежей my_list. Ваша задача — взять каждый первый элемент кортежа и
    создать на его основе название атрибута в классе Empty, а в качестве значения присвоить второй элемент кортежа. В
    итоге в классе Empty  должно появиться десять новых атрибутов."""
    pass


my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]

for i in my_list:
    setattr(Empty, i[0], i[1])


# ------------
class Person:
    """В вашем распоряжении класс Person, у которого имеется 7 атрибутов. Программа будет принимать на вход
    произвольное количество слов в одну строку, разделенных пробелом. Ваша задача проверить, является ли каждое из
    введенных слов названием атрибута. Регистр слов значения не имеет. Нужно вывести в каждой отдельной строке
    введенные слова по порядку и напротив через дефис указать, нашлось свойство с таким именем или нет
    (вывести YES или NO)"""

    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


name_attr = input().split()
for i in name_attr:
    print(f"{i}-{('NO', 'YES')[hasattr(Person, i.casefold())]}")
# ------------
