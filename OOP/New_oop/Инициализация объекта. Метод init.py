# -------------------------------------------------- Инициализация -----------------------------------------------------
# -------------------------------
# ------------

# Для проставления необходимых атрибутов при создании ЭК, есть метод инициализации __init__:
# 1. Каждый магический метод вызывается автоматически, при наступлении своего события;
# 2. Магический метод __init__ будет срабатывать при создании объекта.

class Car:
    """Класс для определения характеристик машин"""

    def __init__(self, new_model, new_engine, new_horse_power):
        print('method init')
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power


bmw_3 = Car('BMW', 3, 500)  # вызывается метод __init__
print(bmw_3.__dict__)
print('-----')
audi_q4 = Car('Audi', 2.5, 400)  # вызывается метод __init__
print(audi_q4.__dict__)
print()
print()


# !!! Цель метода инициализации состоит в том, чтобы проставить наш вновь созданный ЭК нужными атрибутами.
# ------------

# При создании ЭК Python сначала запускает метод-конструктор __new__ для нового объекта и по создаёт пространство имён
# (атрибут __dict__), после которого запускается метод __init__, инициализирующий атрибуты.

class Car:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Car.")
        return super().__new__(cls)

    def __init__(self, new_model, new_engine, new_horse_power):
        print("2. Initialize the new instance of Car.")
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power


bmw_3 = Car('BMW', 3, 500)  # вызывается метод __init__
print(bmw_3.__dict__)


# ------------
# Без передачи аргументов при создании ЭК:
class Car:
    """Класс для определения характеристик машин"""

    def __init__(self, new_model, new_engine, new_horse_power):
        print('method init')
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power


bmw_3 = Car()  # TypeError: Car.__init__() missing 3 required positional arguments...
print(bmw_3.__dict__)


# ------------
# Передача аргументов по-умолчанию:
class Car:
    """Класс для определения характеристик машин"""

    def __init__(self, new_model='Car', new_engine=None, new_horse_power=0):
        print('method init')
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power


bmw_3 = Car()
print(bmw_3.__dict__)
print('-----')
audi_q4 = Car(new_horse_power=350)
print(audi_q4.__dict__)


# ------------
# Получение атрибутов ЭК, при помощи методов словарей:
class Car:
    """Класс для определения характеристик машин"""

    def __init__(self, new_model='Car', new_engine=None, new_horse_power=0):
        print('method init')
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power


auto = Car('BMW', 2.5, 350)
print(*auto.__dict__.values())  # получение значений атрибутов
print(*auto.__dict__.items())  # получение распакованных атрибутов в форме кортежа
print(*auto.__dict__.keys())  # получение ключей словаря
print()
print()


# ---------------------------------------- Создание дополнительных атрибутов -------------------------------------------
# В методе инициализации можно создавать сколько угодно дополнительных атрибутов в экземпляре, проставляя их
# необходимыми значениями:

class Article:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.tags = []  # дополнительные атрибуты для ЭК
        self.likes = 0  # дополнительные атрибуты для ЭК


article = Article('Как надуть грелку', "Пяточок")
print(article.__dict__)  # {'title': 'Как надуть грелку', 'author': 'Пяточок', 'tags': [], 'likes': 0}


# ------------------------------------------------------ Задачи --------------------------------------------------------
class Vehicle:
    """
    Создайте класс Vehicle, у которого есть: Конструктор __init__, принимающий максимальную скорость и пробег.
    Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно.
    """

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


if __name__ == '__main__':
    modelX = Vehicle(200, 18000)
    assert modelX.max_speed == 200
    assert modelX.mileage == 18000
    assert modelX.__dict__ == {'max_speed': 200, 'mileage': 18000}

    audi = Vehicle(240, 5)
    assert audi.__dict__ == {'max_speed': 240, 'mileage': 5}
    print('Good')


# ------------
class Person:
    """
    Перед Василием поставили задачу создать класс Person и реализовать в нем следующие методы:
    __init__ метод, который устанавливает значения атрибутов name и age метод greet, возвращающий строку в следующем
    формате: «Hello, my name is [name], and I am [age] years old»
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old"


if __name__ == '__main__':
    bro = Person('Nikolay', 34)
    assert bro.age == 34
    assert bro.name == 'Nikolay'
    assert bro.greet() == 'Hello, my name is Nikolay, and I am 34 years old'

    sister = Person('Elena', 21)
    assert sister.age == 21
    assert sister.name == 'Elena'
    assert sister.greet() == 'Hello, my name is Elena, and I am 21 years old'

    print('Good')


# ------------
class Laptop:
    """
    Создайте класс Laptop, у которого есть: конструктор __init__, принимающий 3 аргумента: бренд, модель и цену
    ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут
    laptop_name  строковое значение, следующего вида: "<brand> <model>"
    """

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"  # атрибут выводит бренд и модель ноутбука


if __name__ == '__main__':
    laptop1 = Laptop('hp', '15-bw0xx', 57000)
    laptop2 = Laptop('hp', '15-bw0xx', 57000)

    assert isinstance(laptop1, Laptop)
    assert isinstance(laptop2, Laptop)

    hp = Laptop('hp', '15-bw0xx', 57000)
    assert hp.laptop_name == 'hp 15-bw0xx'
    assert hp.price == 57000
    assert isinstance(hp, Laptop)

    lenovo = Laptop('lenovo', 'z-570-dx', 61000)
    assert lenovo.brand == 'lenovo'
    assert lenovo.model == 'z-570-dx'
    assert lenovo.price == 61000
    assert lenovo.laptop_name == 'lenovo z-570-dx'
    assert isinstance(lenovo, Laptop)
    print('Good')


# ------------
class SoccerPlayer:
    """
    Создайте класс SoccerPlayer, у которого есть: Конструктор __init__, принимающий 2 аргумента: name, surname. Также
    во время инициализации необходимо создать 2 атрибута экземпляра: goals и assists — общее количество голов и передач
    игрока, изначально оба значения должны быть 0. Метод score, который принимает количество голов, забитых игроком.
    По умолчанию данное значение равно единице. Метод должен увеличить общее количество забитых голов игрока на
    переданное значение. Метод make_assist, который принимает количество передач, сделанных игроком за матч. По
    умолчанию данное значение равно единице. Метод должен увеличить общее количество сделанных передач игроком на
    переданное значение.
    Метод statistics, который выводит статистику игрока в виде: <Фамилия> <Имя> - голы: <goals>, передачи: <assists>
    """

    def __init__(self, name: str, surname: str) -> None:
        self.name, self.surname = name, surname
        self.goals, self.assists = 0, 0

    def score(self, value_goals: int = 1) -> None:
        self.goals += value_goals

    def make_assist(self, value_assists: int = 1) -> None:
        self.assists += value_assists

    def statistics(self) -> None:
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")


if __name__ == '__main__':
    leo = SoccerPlayer('Leo', 'Messi')
    assert isinstance(leo, SoccerPlayer)
    assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
    leo.score(700)
    assert leo.goals == 700
    leo.make_assist(500)
    assert leo.assists == 500

    leo.statistics()

    kokorin = SoccerPlayer('Alex', 'Kokorin')
    assert isinstance(kokorin, SoccerPlayer)
    assert kokorin.name == 'Alex'
    assert kokorin.surname == 'Kokorin'
    assert kokorin.assists == 0
    assert kokorin.goals == 0
    kokorin.score()
    assert kokorin.goals == 1
    kokorin.score(5)
    assert kokorin.goals == 6
    kokorin.make_assist()
    assert kokorin.assists == 1
    kokorin.make_assist(10)
    assert kokorin.assists == 11

    kokorin.statistics()

    obi = SoccerPlayer('Оби-Ван', 'Кеноби')
    obi.make_assist()
    assert obi.name == 'Оби-Ван'
    assert obi.surname == 'Кеноби'
    assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}

    obi.statistics()

    mila = SoccerPlayer('Mila', 'Kunis')
    mila.make_assist()

    mila.statistics()


# ------------

class Zebra:
    """
    Создайте класс Zebra, у которого метод which_stripe поочередно печатает фразы «Полоска белая»,
    «Полоска черная» без кавычек, начиная именно с фразы «Полоска белая». Также реализуйте метод run_away, который
    печатает фразу «Oh, Sugar Honey Ice Tea».
    """
    __PHRASES = ["Полоска белая", "Полоска черная"]

    def __init__(self):
        self.count = 0

    def which_stripe(self):
        print(self.__PHRASES[self.count])
        if self.count == 1:
            self.count = -1
        self.count += 1

    def run_away(self):
        print("Oh, Sugar Honey Ice Tea")


if __name__ == '__main__':
    zebra = Zebra()
    zebra.run_away()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.run_away()


# ------------
class Person:
    """
    Создайте класс Person, у которого есть: Конструктор __init__, принимающий имя, фамилию и возраст. Их необходимо
    сохранить в атрибуты экземпляра first_name , last_name, age. Метод full_name, который возвращает строку в виде
    "<Фамилия> <Имя>". Метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае.
    """

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def is_adult(self) -> bool:
        return self.age >= 18


if __name__ == '__main__':
    p1 = Person('Ash', 'Ketchum', 20)
    assert isinstance(p1, Person)
    assert p1.full_name() == 'Ketchum Ash'
    assert p1.age == 20
    assert p1.first_name == 'Ash'
    assert p1.last_name == 'Ketchum'
    assert p1.is_adult() is True

    p2 = Person('Hermione', 'Granger', 16)
    assert isinstance(p2, Person)
    assert p2.age == 16
    assert p2.first_name == 'Hermione'
    assert p2.last_name == 'Granger'
    assert p2.full_name() == 'Granger Hermione'
    assert p2.is_adult() is False
    print('Good')


# ------------
class Rectangle:
    """
    Создайте класс Rectangle, имеющий следующие методы:
    1. метод __init__, устанавливает значения атрибутов width и height;
    2. метод area, возвращает площадь прямоугольника;
    3. метод perimeter, возвращает периметр прямоугольника.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return self.width * 2 + self.height * 2


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    assert r1.width == 2
    assert r1.height == 3
    assert r1.perimeter() == 10
    assert r1.area() == 6

    r2 = Rectangle(10, 0.5)
    assert r2.width == 10
    assert r2.height == 0.5
    assert r2.perimeter() == 21.0
    assert r2.area() == 5.0
    print('Good')


# ------------

class Numbers:
    """
    Реализуйте класс Numbers, который предназначен для хранения произвольного количества чисел. Данный класс должен
    содержать:
    1. метод __init__, принимающий произвольное количество чисел и сохраняющих их внутри экземпляр;
    2. метод add_number, принимает числовое значение и добавляет его в конец коллекции экземпляра;
    3. метод get_positive, возвращает список всех положительных чисел из коллекции экземпляра;
    4. метод get_negative, возвращает список всех отрицательных чисел из коллекции экземпляра;
    5. метод get_zeroes, возвращает список всех нулевых значений из коллекции экземпляра.
    """

    def __init__(self, *args):
        self.array = [*args]

    def add_number(self, num):
        self.array.append(num)

    def get_positive(self):
        return list(filter(lambda x: x > 0, self.array))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.array))

    def get_zeroes(self):
        return list(filter(lambda x: x == 0, self.array))


if __name__ == '__main__':
    nums = Numbers()
    print(nums.get_positive())
    print(nums.get_negative())
    print(nums.get_zeroes())

    nums.add_number(5)
    nums.add_number(3)
    nums.add_number(4)

    print(nums.get_positive())
    print(nums.get_negative())
    print(nums.get_zeroes())


# ------------
class Worker:
    """
    Создайте класс Worker, у которого есть: метод __init__, принимающий 4 аргумента: имя, зарплата, пол и паспорт.
    Необходимо сохранить их в следующих атрибутах: name, salary, gender и passport. Метод get_info, который распечатает
    информацию о сотруднике в следующем виде: «Worker {name}; passport-{passport}»
    """

    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f"Worker {self.name}; passport-{self.passport}")


persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

worker_objects = [Worker(*i) for i in persons]

for i in worker_objects:
    i.get_info()
# ------------
