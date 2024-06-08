# ----------------------------------------- Декораторы класса: @property, @classmethod ---------------------------------

# Инкапсуляция — это одна из основ объектно-ориентированного программирования, которая говорит нам о том, что поля
# (переменные) класса и его методы (функции класса) надо объединять в одну целую систему.

# Декораторы — это определённые штуки в языке Python, которые позволяют менять поведение функции
# (или, как вы сейчас убедитесь, и метода), не меняя её исходного кода.

# ---------------------------------------------- @property -------------------------------------------------------------

# создадим класс собаки
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property  # тот самый магический декоратор
    def human_age(self):
        return self.age * 7.3


janne = Dog("jane", 4)
# т.к. метод помечен декоратором property, то нам не надо вызывать этот метод, чтобы получить результат
print(janne.human_age)


# геттеры — это специальные методы для получения значения поля класса;
# сеттеры — это специальные методы для установки значений в поле класса.

class Dog:
    _happiness = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле - шкала счастья
    @property
    def happiness(self):
        return self._happiness

    # декораторы .setter должны называться так же, как и метод, помеченный декоратором @property, для которого
    # вы хотите устанавливать значение, иначе интерпретатор выдаст ошибку.
    @happiness.setter
    # с помощью декоратора setter мы можем неявно передать во второй
    # аргумент значение, находящееся справа от равно, а не закидывать это
    # значение в скобки, как мы это делали в модуле C1, когда не знали о
    # декораторах класса
    def happiness(self, value):
        if 0 <= value <= 100:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
print(jane.happiness)


# ---------------------------------------------- @classmethod ----------------------------------------------------------

class ParentClass:

    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


# Вызываем методы класса через класс.
ParentClass.method(0)  # ParentClassclassmethod. 0
ParentClass.call_original_method()  # ParentClassclassmethod. 5

ChildClass.method(0)  # ChildClassclassmethod. 0
ChildClass.call_original_method()  # ChildClassclassmethod. 6

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_class_method()  # ParentClassclassmethod. 10


class Square:
    s = None  # сторона квадрата

    def __init__(self, a):
        self.a = a

    @property
    def area(self):  # метод по вычислению
        return self.a ** 2

    @property
    def a1(self):  # геттер
        return self.s

    @a1.setter
    def a1(self, value):  # сеттер, задекорированный от геттера
        if value > 0:
            self.s = value


f = Square(5)

print(f.area)
