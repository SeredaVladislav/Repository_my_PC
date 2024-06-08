class User:
    pass


peter = User()  # Экземпляр Класса
peter.name = "Peter Robertson"  # .right_name - Атрибут экземпляра Класса

julia = User()  # Экземпляр Класса
julia.name = "Julia Donaldson"  # .right_name - Атрибут экземпляра Класса

print(peter.name)
print(julia.name)


# ----------------------------------------------------------------------------------------------------------------------

class Users:
    number_of_fingers = 5  # Атрибут Класса
    number_of_eyes = 2  # Атрибут Класса


lancelot = Users()  # Экземпляр Класса
print(lancelot.number_of_fingers)  # Вывод Экземпляра Класса с Атрибутом
print(lancelot.number_of_eyes)  # Вывод Экземпляра Класса с Атрибутом


# ----------------------------------------------- Магический метод __init__ --------------------------------------------


class User3:
    def __init__(self, name, email):  # Метод Класса (Конструктор)
        self.name = name  # Атрибут Класса
        self.email = email  # Атрибут Класса


peter = User3(name="Peter Robertson", email="peterrobertson@mail.com")  # Экземпляр Класса
julia = User3(name="Julia Donaldson", email="juliadonaldson@mail.com")  # Экземпляр Класса

print(peter.name)
print(julia.email)


# ----------------------------------------------- Методы и функции -----------------------------------------------------


class Product:
    def __init__(self, name, category, quantity_in_stock):  # Метод Класса (Конструктор)
        self.name = name  # Атрибут Класса
        self.category = category  # Атрибут Класса
        self.quantity_in_stock = quantity_in_stock  # Атрибут Класса

    def is_available(self):  # Метод Класса
        return True if self.quantity_in_stock > 0 else False  # Условие Метода Класса


eggs = Product("eggs", "food", 5)  # Экземпляр Класса
print(eggs.is_available())  # Вызов Экземпляра с отработкой условия через Метод Класса is_available()

# ----------------------------------------------------------------------------------------------------------------------

events = [
    {
        "timestamp": 1554583508000,
        "event_type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "event_type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "event_type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.event_type = event_type
        self.session_id = session_id


for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("event_type"),
                      session_id=event.get("session_id"))  # метод словаря .get() вызывает значение Ключа в Словаре
    print(event_obj.timestamp)

print()

# ----------------------------------------------------------------------------------------------------------------------

events = [
    {
        "timestamp": 1554583508000,
        "event_type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "event_type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "event_type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):  # Метод Класса (Конструктор)
        self.timestamp = timestamp  # Атрибут Класса
        self.type = event_type  # Атрибут Класса
        self.session_id = session_id  # Атрибут Класса

    def init_from_dict(self, event_dict):  # Метод Класса
        self.timestamp = event_dict.get("timestamp")  # Атрибут Метода с ключами будущего Словаря
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")


for event in events:  # Перебор Словаря
    event_obj = Event()  # Создаем Экземпляр Класса
    event_obj.init_from_dict(event)  # К Экземпляру применяем метод init_from_dict с Аргументом цикла
    print(event_obj.timestamp)


# --------------------------------------------------- Инкапсуляция------------------------------------------------------
class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age  # Геттер просто возвращает значение поля и не принимает никаких аргументов

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age, int):  # проверяем, что человеку больше 0 лет и его возраст - целое число
            self.age = age  # Сеттер принимает один аргумент — значение, которое он должен установить в поле


h = Human()
h.set_age(15)
print(h.get_age())

print()

# --------------------------------------------------- Наследование -----------------------------------------------------


import datetime


class Product:
    max_quantity = 100000  # Атрибуты Родительского Класса

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):  # Методы Родительского Класса
        return True if self.quantity_in_stock > 0 else False


class Food(Product):  # Производный Класса(Наследованный Класс)
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)  # Экземпляр Класса Food
# Экземпляр Класса Food, использовал конструктор Родительского Класса

print(eggs.max_quantity)
print(eggs.is_available())


# ----------------------------------------------------------------------------------------------------------------------
class A:  # Класс A
    def getVal(self):
        return 5  # Вывод 5


class B(A):  # Наследование Класса A
    def getVal(self):
        return super().getVal() * 2  # Вывод из Класса A (5) * 2 = 10


class C(B):  # Наследование Класса B
    def getVal(self):
        return super().getVal() * 2 * 2  # Результат Класса B (10) * 2 * 2 = 40


class D(A):
    def getVal(self):
        return super().getVal() * 2 * 2


if __name__ == "__main__":
    a = C()  # Экземпляр Класса C с результатом 40
    print(a.getVal())


# Примечание:

# В Python метод super() используется для вызова метода из родительского класса или суперкласса.
# Он позволяет вызвать метод из родительского класса, даже если класс наследуется от другого класса.

# Пример использования метода super():

class A:
    def foo(self):
        print("A'count foo")


class B(A):
    def bar(self):
        super().foo()  # вызов метода A'count foo из класса B


b = B()
b.bar()  # выводит "A'count foo"

# В данном примере класс B наследуется от класса A.
# Метод bar() в классе B вызывает метод foo() из класса A с помощью super(),
# который позволяет обратиться к методам базового класса.


# ------------------------------------------------- if __name__ == "__main__": -----------------------------------------

# Оператор if __name__ == '__main__': используется в Python для определения того,
# является ли текущий скрипт исполняемым файлом. Если это так, то код внутри блока if будет выполнен,
# иначе он будет пропущен.

# Этот оператор используется для того, чтобы убедиться, что скрипт запускается из командной строки
# или другого исполняемого файла, а не импортируется из другого скрипта. Если скрипт импортируется,
# то оператор if не будет выполнен и код внутри него не будет выполнен.

# Например, предположим, что у нас есть скрипт myscript.py, который содержит следующий код:

if __name__ == '__main__':
    print('Это исполняемый файл')
else:
    print('Этот скрипт импортируется')


# Если мы запустим этот скрипт из командной строки, то он выведет сообщение “Это исполняемый файл”.
# Если же мы импортируем этот скрипт из другого скрипта, то сообщение не будет выведено,
# так как оператор if не выполнится.


# См. _1_файл.py и _2_файл.py

# ----------------------------------------------- Наследование (далее) -------------------------------------------------

class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):  # Метод-Конструктор Родительского Класса
        self.timestamp = timestamp  # Атрибуты Родительского Класса
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):  # Метод Родительского Класса
        self.timestamp = event_dict.get("timestamp")  # Атрибут Класса (Вывод значения Словаря по Ключу)
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("Это общее событие.")


class ItemViewEvent(Event):  # дочерний Класс
    type = "itemViewEvent"  # переопределенный Атрибут Родительского Класса

    def __init__(self, timestamp=0, session_id="", number_of_views=0):  # переопределили Конструктор Класса
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):  # переопределенный Метод Родительского Класса
        print("Это событие означает, что кто-то просмотрел элемент.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)


# ----------------------------------------------- Множественное Наследование -------------------------------------------

# См.Flat.py

# ---------------------------------------------------- Импорт Классов --------------------------------------------------

# См.CatTest.py и CatReturn.py


# ---------------------------------------------------- Полиморфизм -----------------------------------------------------

# См.директория python_practice/rectangle.py и rectangle_2.py

# ------------------------------------------- Магические методы на примере __eq__ и __str__ ----------------------------

# Перегрузка представляет собой изменение поведения стандартного оператора или метода под особенности класса.
# Возьмем несколько наиболее часто используемых методов:

# __eq__ — определяет поведение оператора равенства ==;
# __str__ — определяет поведение функции str() или вызов внутри функции print().

# См.points.py

# ------------------------------------------------------ Практика ------------------------------------------------------

class Rectangle:  # Класс Прямоугольник
    def __init__(self, x, y, wight, height):  # Атрибуты Класса в Конструкторе
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def __str__(self):  # Метод, для возврата Атрибутов как str  (Переопределение функции str)
        return f"Rectangle : {self.x}, {self.y}, {self.wight}, {self.height}."

    def get_area(self):  # Метод для подсчета площади прямоугольника
        return self.wight * self.height


f = Rectangle(5, 10, 50, 100)  # Экземпляр Класса
print(str(f))  # Вывод Атрибутов в виде строки

print(f.get_area())  # Вывод результата подсчета площади прямоугольника


# ----------------------------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def __str__(self):  # Перегрузка функции str
        return f"{self.name} {self.lastname}. {self.city}. Баланс:{self.balance} руб."


f = Person("Иван", "Петров", "Москва", 50)

print(f)


# ----------------------------------------------------------------------------------------------------------------------

class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city = city

    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):  # Метод для вывода только интересующей информации
        return f'{self.first_name} {self.second_name},г. {self.city}'


costomer_1 = Customers('Иван', 'Петров', 'Москва', 50)  # Экземпляры Класса отдельного человека
costomer_2 = Customers('Владимир', 'Зайцев', 'Кострома', 50)
costomer_3 = Customers('Олеся', 'Янина', 'Новосибирск', 50)

guest_list = [costomer_1, costomer_2, costomer_3]  # Переменная с экземплярами Класса

for guest in guest_list:  # Цикл для перебора всех экземпляров Класса
    print(guest.get_guest())  # Вывод инфо применяя метод с интересующими аргументами Класса
