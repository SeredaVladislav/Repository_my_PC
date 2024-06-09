# -------------------------------------------------- Атрибуты-функции --------------------------------------------------
# -------------------------------
# ------------

class Car:
    """Класс для определения характеристик машин"""
    model = "BMW"
    engine = 1.6

    def drive(self):
        print(f"Let's go")


a = Car()  # Создаём экземпляр класса
a.drive()  # Вызываем метод класса


# --------------------------------- Получение и изменение атрибутов экземпляра в методах -------------------------------
class Car:
    """Класс для определения характеристик машин"""
    model = "VAZ"
    engine = 1.6
    horse_power = 100
    color = ''

    def drive(self):
        print(f"Let's go {self.model} {self.engine}")

    def power(self):
        print(f'Мощность {self.model} - {self.horse_power} лошадиных сил')

    def set_color(self):
        print(f'Цвет {self.model} - {self.color}')

    def set_values(self, new_model, new_engine, new_horse_power, new_color):
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power
        self.color = new_color


auto = Car()
auto.drive()  # Let's go VAZ 1.6

auto.model = 'BMW'  # Поменяем машину
auto.drive()  # Let's go BMW 1.6
auto.power()  # Мощность BMW - 100 лошадиных сил

auto.horse_power = 350  # Добавим лошадок к мощности
auto.power()  # Мощность BMW - 350 лошадиных сил

auto.set_values('AUDI', 5, 300, 'blue')
auto.drive()  # Let's go AUDI 5
auto.power()  # Мощность AUDI - 300 лошадиных сил
auto.set_color()  # Цвет AUDI - blue


# ------------------------------------------- Вызов методов через класс ------------------------------------------------

# При вызове через класс метода-функции, произойдет ошибка, так как не передается обязательный аргумент:
class Car:
    """Класс для определения характеристик машин"""
    model = "BMW"
    engine = 1.6

    def drive(self):
        print("Let's go")

    def color_car(self):
        print('Вызов цвета машины')


Car.color_car()  # TypeError: Car.color_car() missing 1 required positional argument: 'self'


# Вызов метода, через экземпляр класса в виде аргумента методу:
class Car:
    """Класс для определения характеристик машин"""
    model = "BMW"
    engine = 1.6

    def drive(self):
        print("Let's go")

    def color_car(self):
        print('Вызов цвета машины')


a = Car()
Car.color_car(a)  # Вызов цвета машины
Car.drive(a)  # Let's go


# По сути, вызов Car.color_car(a) становится эквивалентным a.color_car().


class Car:
    """Класс для определения характеристик машин"""
    model = "BMW"
    engine = 1.6

    def set_color_car(self, color):
        self.color = color
        print(f'Теперь у машины {self.color} цвет')

    def get_color_car(self):
        return self.color


a = Car()  # Создаём экземпляр класса a
b = Car()  # Создаём экземпляр класса b

a.set_color_car('black')  # Теперь у машины black цвет
print('Атрибуты ЭК a:', a.__dict__)  # проверяем наличие данного атрибута в a

b.set_color_car('red')  # Теперь у машины red цвет
print('Атрибуты ЭК b:', b.__dict__)  # проверяем наличие данного атрибута в b

print(a.get_color_car(), b.get_color_car())  # Получаем значения из метода

# ------------------------------------------------------ Задачи --------------------------------------------------------
"""
Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!
"""


class Lion:

    def roar(self):
        print(f"Rrrrrrr!!!")


if __name__ == '__main__':
    simba = Lion()
    simba.roar()  # Rrrrrrr!!!
# ------------
"""
    Создайте класс Robot, в котором реализованы:
    Метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
    Метод say_bye ,  печатающий на экран фразу «See u later alligator»
    После определения класса создайте 2 экземпляра и сохраните их в переменные  c3po и r2d2
    Затем вызовите у переменной  c3po  метод say_hello , а затем метод say_bye
    И то же самое сделайте с переменной r2d2:  вызовите метод say_hello , потом — метод say_bye
"""


class Robot:
    def say_hello(self):
        print(f"Hello, human! My name is C-3PO")

    def say_bye(self):
        print(f"See u later alligator")


if __name__ == '__main__':
    c3po, r2d2 = (Robot() for _ in range(2))
    c3po.say_hello(), c3po.say_bye()
    r2d2.say_hello(), r2d2.say_bye()
# ------------
"""
    В предыдущей задаче вы могли обратить внимание на то, что выводится всегда одно и то же имя робота в методе 
    say_hello. Давайте это исправим при помощи атрибута экземпляра name . Для этого переопределяем класс Robot, 
    в котором должны быть реализованы:
    Метод set_name, принимающий имя робота и сохраняющий его в атрибуте экземпляра name 
    Метод say_hello. Метод должен проверить, есть ли у ЭК атрибут name . Если атрибут name  присутствует, необходимо 
    напечатать фразу «Hello, human! My name is <name>». Если атрибут name  отсутствует у экземпляра, печатайте 
    сообщение «У робота нет имени» 
    Метод say_bye, печатающий на экран фразу «See u later alligator»
"""


class Robot:
    def say_hello(self):
        if hasattr(self, 'name'):
            print(f"Hello, human! My name is {self.name}")
        else:
            print(f"У робота нет имени")

    def say_bye(self):
        print(f"See u later alligator")

    def set_name(self, value):
        self.name = value


if __name__ == '__main__':
    c3po = Robot()
    c3po.say_hello()
    c3po.set_name('R2D2')
    c3po.say_hello()
    c3po.say_bye()

    r = Robot()
    r.set_name('Chappy')
    r.say_hello()

    d = Robot()
    d.say_hello()
    d.set_name('Wally')
    d.say_hello()
# ------------

"""
    Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения. В классе Counter нужно 
    определить:
    Метод start_from, который принимает один необязательный аргумент. Значение, с которого начинается подсчет, по 
    умолчанию равно 0. Метод increment, который увеличивает счетчик на 1. Метод display, который печатает фразу 
    "Текущее значение счетчика = <value>". Метод reset,  который обнуляет накопившееся значение счетчика.
"""


class Counter:

    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.value}")

    def reset(self):
        self.value = 0


c1 = Counter()
c2 = Counter()

assert isinstance(c1, Counter)  # Является ли ЭК определенным с классом Counter()
assert isinstance(c2, Counter)  # Является ли ЭК определенным с классом Counter()
assert c1.__dict__ == {}  # Имеют ли ЭК методы или аргументы
assert c2.__dict__ == {}  # Имеют ли ЭК методы или аргументы

c1.start_from(45)  # Передача методу значения 45
assert len(c1.__dict__) == 1  # Появился ли метод в ЭК

c1.increment()  # 45 + 1
c1.display()  # печатает 46
c1.increment()  # 46 + 1
c1.display()  # печатает 47

c2.start_from()  # 0
c2.display()  # печатает 0
c2.increment()  # 0 + 1
c2.display()  # печатает 1

c1.reset()  # обнулили с1, но с2 не должен меняться

c1.display()  # печатает 0
c2.display()  # по прежнему печатает 1
# ------------

"""
    Создайте класс Constructor, в котором реализованы: Метод add_atribute, принимающий на вход название атрибута в 
    виде строки и его значение. При помощи функции setattr необходимо создать или изменить атрибут для ЭК, у которого
    этот метод был вызван. Метод display, печатающий на экран словарь __dict__ у ЭК.
"""


class Constructor:

    def add_atribute(self, name, value):
        setattr(self, name, value)  # Функция создает или изменяет атрибут для ЭК.

    def display(self):
        print(self.__dict__)  # Выводит словарь атрибутов и методов ЭК.


if __name__ == '__main__':
    obj1 = Constructor()
    assert obj1.__dict__ == {}
    obj1.display()
    obj1.add_atribute('color', 'red')
    assert obj1.color == 'red'
    obj1.add_atribute('width', 20)
    assert obj1.width == 20
    obj1.display()

    obj2 = Constructor()
    obj2.display()
    obj2.add_atribute('height', 100)
    assert obj2.height == 100
    obj2.display()

    obj3 = Constructor()
    obj3.display()
    obj3.add_atribute('a', 100)
    obj3.add_atribute('b', 300)
    obj3.add_atribute('c', 200)
    obj3.add_atribute('b', 1)
    assert obj3.__dict__ == {'a': 100, 'b': 1, 'c': 200}
    obj3.display()

# ------------
"""
    Создайте класс Point. У этого класса должны быть:
    Метод set_coordinates, который принимает координаты точки на плоскости и сохраняет их в экземпляр класса в атрибуты
    x и y. Метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между 
    двумя точками по теореме Пифагора. В случае, если в данный метод передается не экземпляр класса Point, необходимо
    вывести сообщение "Передана не точка".
"""


class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, value):
        if isinstance(value, Point):
            return ((value.x - self.x) ** 2 + (value.y - self.y) ** 2) ** 0.5
        else:
            print(f"Передана не точка")


if __name__ == '__main__':
    p1 = Point()
    p2 = Point()
    assert isinstance(p1, Point)
    assert isinstance(p2, Point)

    p1.set_coordinates(1, 2)
    assert p1.x == 1
    assert p1.y == 2
    p2.set_coordinates(4, 6)
    assert p2.x == 4
    assert p2.y == 6
    assert p1.get_distance(p2) == 5.0

    p3 = Point()
    p3.set_coordinates(10, 10)
    p1.set_coordinates(4, 2)
    assert p1.get_distance(p3) == 10.0
    res = p1.get_distance(10)
    assert res is None

    assert p2.get_distance([1, 2, 3]) is None
# ------------
