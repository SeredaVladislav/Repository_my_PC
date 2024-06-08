# ---------------------------------------------- Инкапсуляция ----------------------------------------------------------

# Инкапусляция — это один из принципов OOP, который говорит нам о том, что поля и методы должны быть одной целой
# системой. Иначе говоря, работаем с полями класса только через методы.


# Пример неправильного кода.
# Создаём неправильный класс.
class Human:
    # класс человек с полем возраста
    age = None

    def __init__(self, age=4):
        self.age = age


h = Human()
h.age = 15  # (Так делать лучше не стоит, если вы хотите когда-нибудь найти работу)
print(h.age)  # и так тоже


#  Более правильный пример
# Исправим наш предыдущий код.
class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age, int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст -
            # целое число
            self.age = age


h = Human()
h.set_age(15)
print(h.get_age())

# Геттеры — пишется так: get_<имя поля>. Геттер просто возвращает значение поля и не принимает никаких аргументов.
# Основная задача геттера — не давать изменять атрибут класса вне класса. Это значит, что при использовании обычной
# переменной age её можно будет изменить в основном коде:

h.age = 11
print(h.age)

# С геттером так не получится. Используя геттер, вы явно указываете в коде, что значение только для чтения.
# Вы можете получить его, но не можете изменить.

print(h.get_age())


# Это своеобразная защита для других разработчиков. Используя функцию get_age() нельзя случайно задать ему значение.

# Сеттер — пишется так: set_<имя поля>. Сеттер принимает один аргумент — значение, которое он должен установить в поле.


class Javatpoint:
    def __init__(self):
        self._age = 0
        # using the get function

    def get_age(self):
        print("getter method")
        return self._age
        # using the set function

    def set_age(self, y):
        print("setter method")
        self._age = y
        # using the del function

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)  # Позволяет использовать методы как атрибут age


John = Javatpoint()

John.age = 18

print(John.age)


# ----------------------------------------------------------------------------

# Приватные атрибуты и методы:  (например, __private_attribute)
class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def __private_method(self):
        print('Это приватный метод')


if __name__ == "__main__":
    f = MyClass()
    print(f.__private_method)  # метод не доступен для внешнего вызова
    # (AttributeError: 'MyClass' object has no attribute '__privat_method')


# Защищенные атрибуты и методы:  (например, _protected_attribute)
class MyClass:
    def __init__(self):
        self._protected_attribute = 42

    def _protected_method(self):
        print('Это защищенный метод')


if __name__ == "__main__":
    g = MyClass()
    print(g._protected_method())  # Вызов метода возможен, предназначен для внутреннего использования в классе
    # (но по договоренности между программистами, он является защищенным)


# Публичные методы и классы:
class MyClass:
    def __init__(self):
        self.public_attribute = 42

    def public_method(self):
        print('This is a public method')


if __name__ == "__main__":
    s = MyClass()
    print(s.public_method())  # Метод является публичным и может быть использован для вывода


# -----------------------------

# получение доступа к приватному методу или атрибуту:

class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def __private_method(self):
        print('Это приватный метод')


obj = MyClass()

# Попытка напрямую получить доступ к приватному атрибуту вызовет ошибку
# print(obj_func.__private_attribute)

# Попытка напрямую вызвать приватный метод вызовет ошибку
# obj_func.__private_method()

# Однако, с помощью right_name mangling(искажение) можно получить доступ к приватному атрибуту и методу:
print(obj._MyClass__private_attribute)  # Вывод: 42
obj._MyClass__private_method()  # Вывод: Это приватный метод
