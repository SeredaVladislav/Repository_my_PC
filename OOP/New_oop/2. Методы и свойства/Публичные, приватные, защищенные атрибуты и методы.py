# ------------------------------------------- Уровни доступа атрибутов и методов ---------------------------------------
# -------------------------------
# ------------

# Уровни доступа к атрибутам и методам:
# 1. Публичный (public)
# 2. Защищенный (protected)
# 3. Приватный (private)

# ----------------------------------------------------------------------------------------------------------------------
# Публичный (public) уровень:

class BankAccount:

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.passport = password

    def print_data(self):
        print(self.name, self.balance, self.passport)


if __name__ == '__main__':
    account1 = BankAccount('Bob', 10500, 2412_13966)
    print(account1.name, account1.balance, account1.passport, sep='\n')
    # Bob
    # 10500
    # 241213966


# ----------------------------------------------------------------------------------------------------------------------
# Защищенный (protected) уровень:
# Работают исключительно на уровне соглашения. Не скрывают атрибуты и методы функционально.

class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name  # нижним подчеркиванием указываем
        self._balance = balance  # что атрибут должен быть защищен
        self._passport = passport  # от публичного доступа

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)


if __name__ == '__main__':
    account1 = BankAccount('Bob', 100000, 45484564654)
    account1.print_protected_data()
    print(account1._name)
    print(account1._balance)
    print(account1._passport)
    # Bob 100000 45484564654
    # Bob
    # 100000
    # 45484564654


# ----------------------------------------------------------------------------------------------------------------------
# Приватный (private) уровень:

class BankAccount:

    def __init__(self, name, balance, passport) -> None:
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self) -> tuple:
        return self.__name, self.__balance, self.__passport


if __name__ == '__main__':
    account1 = BankAccount('Bob', 100000, 45484564654)
    print(account1.print_private_data())


# ------------
# Обращение к атрибутам через специально созданный метод:
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        return self.__name, self.__balance, self.__passport


if __name__ == '__main__':
    account1 = BankAccount('Bob', 100000, 45484564654)
    print(account1.__name)  # AttributeError
    print(account1.__balance)
    print(account1.__passport)


# AttributeError: 'BankAccount' object has no attribute '__name'


# ------------
# Аналогичная ситуация и с приватным методом: вне класса нельзя обратиться к его имени, внутри класса мы можем это
# сделать. В примере ниже мы вызываем приватный метод __print_private_data внутри открытого метода public_call:

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def public_call(self):
        print('work public method')
        self.__print_private_data()

    def __print_private_data(self):
        print('work private method')
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
account1.public_call()


# work public method
# work private method
# Bob 100000 45484564654


# ----------------------------------------------------------------------------------------------------------------------
# Доступ к приватным атрибутам и методам вне класса:

# Обратиться к приватным атрибутам в обход разрешенного доступа через метод print_private_data вполне возможно. Для
# этого мы можем узнать список имен, доступных в нашем классе,  при помощи функции dir:

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def public_call(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
print(dir(account1))  # просмотр атрибутов нашего экземпляра класса


# [
# '_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', '_BankAccount__print_private_data',
# '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'public_call'
# ]


# Обратите внимание на такие названия, как:
# _BankAccount__balance
# _BankAccount__name
# _BankAccount__passport
# _BankAccount__print_private_data

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def public_call(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
print(account1._BankAccount__balance)
print(account1._BankAccount__name)
print(account1._BankAccount__passport)
account1._BankAccount__print_private_data()


# 100000
# Bob
# 45484564654
# Bob 100000 45484564654

# ---------------------------------------------------- Задачи ----------------------------------------------------------

class PizzaMaker:
    """Вызывать защищенные и приватные методы у экземпляров класса"""

    def __make_pepperoni(self):
        print('Приватный метод вызван!')

    def _make_barbecue(self):
        print('Защищенный метод вызван!')


if __name__ == '__main__':
    maker = PizzaMaker()
    maker._make_barbecue()  # Защищенный метод вызван
    maker._PizzaMaker__make_pepperoni()  # Приватный метод вызван!


# ------------
class AverageCalculator:
    """Вызвать приватный метод вне класса"""

    def __init__(self, numbers) -> None:
        self.numbers = numbers

    def __calculate_average(self) -> int:
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
print(average_calculator._AverageCalculator__calculate_average())


# ------------
class Student:
    """Создайте класс Student, у которого есть:
    1. конструктор __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;

    2. приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
    2.1 Имя: <name>
    2.2 Возраст: <age>
    2.3 Направление: <branch>

    3. метод access_private_method, который вызывает приватный метод __display_details."""

    def __init__(self, name, age, branch) -> None:
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f"Имя: {self.__name}\n"
              f"Возраст: {self.__age}\n"
              f"Направление: {self.__branch}")

    def access_private_method(self):
        self.__display_details()


if __name__ == '__main__':
    adam = Student("Adam Smith", 25, "Information Technology")
    piter = Student("Piter Parker", 34, "Information Security")

    adam.access_private_method()
    assert piter._Student__age == 34, 'Где приватный атрибут __age?'
    assert piter._Student__branch == "Information Security", 'Где приватный атрибут __branch?'
    assert piter._Student__name == "Piter Parker", 'Где приватный атрибут __name?'
    piter.access_private_method()
    adam._Student__display_details()
    piter._Student__display_details()
    # Имя: Adam Smith
    # Возраст: 25
    # Направление: Information Technology
    # Имя: Piter Parker
    # Возраст: 34
    # Направление: Information Security
    # Имя: Adam Smith
    # Возраст: 25
    # Направление: Information Technology
    # Имя: Piter Parker
    # Возраст: 34
    # Направление: Information Security


# ------------
class BankDeposit:
    """Создайте класс BankDeposit, имеет следующие методы:
    1. Метод __init__, который устанавливает значения атрибутов name, balance и rate:
    1.1 владелец депозита,
    1.2 значение депозита
    1.3 годовая процентная ставка.

    2. Приватный метод __calculate_profit, возвращает количество денег, которое заработает владелец счета через
    год с учетом его годовой ставки.

    3. Публичный метод get_balance_with_profit, возвращает общее количество средств, которое будет у владельца
    депозита через год."""

    def __init__(self, name: str, balance: int, rate: int) -> None:
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self) -> float:
        result = self.balance * (self.rate / 100)
        return result

    def get_balance_with_profit(self) -> float:
        return self.balance + self.__calculate_profit()


if __name__ == '__main__':
    account = BankDeposit("John Connor", 1000, 5)
    assert account.name == "John Connor"
    assert account.balance == 1000
    assert account.rate == 5
    assert account._BankDeposit__calculate_profit() == 50.0
    assert account.get_balance_with_profit() == 1050.0

    account_2 = BankDeposit("Sarah Connor", 200, 27)
    assert account_2.name == "Sarah Connor"
    assert account_2.balance == 200
    assert account_2.rate == 27
    assert account_2._BankDeposit__calculate_profit() == 54.0
    assert account_2.get_balance_with_profit() == 254.0
    print('Good')
# ------------
class Library:
    """
    Создайте класс Library, имеющий следующие методы:
    1. Метод __init__, который принимает список названий книг и сохраняет его в приватном атрибуте __books.

    2. Приватный метод check_availability, который принимает название книги и возвращает True, если книга присутствует в
    библиотеке, в противном случае возвращается False.

    3. Публичный метод search_book, который ищет книгу в библиотеке при помощи приватного метода check_availability.
    Возвращает True, если нашел,  иначе False.

    4. Публичный метод return_book, принимает название книги, которую нужно вернуть в библиотеку (добавить в конец
    атрибута __books), ничего возвращать не нужно.

    5. Защищенный метод checkout_book, который принимает на вход название книги. Если книга имеется в наличии, ее
    необходимо выдать читателю и удалить из списка книг. Метод в таком случае должен вернуть True, как знак того, что
    операция выдачи книги прошла успешно. Если книга отсутствовала, необходимо вернуть False.
    """

    def __init__(self, books: list) -> None:
        self.__books = books

    def __check_availability(self, name_book) -> bool:
        return name_book in self.__books

    def search_book(self, name_b) -> bool:
        return self.__check_availability(name_b)

    def return_book(self, add_name_book) -> None:
        self.__books.append(add_name_book)

    def _checkout_book(self, name_book) -> bool:
        if name_book not in self.__books:
            return False
        self.__books.remove(name_book)
        return True


if __name__ == '__main__':
    library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

    assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
    assert library.search_book("Moby-Dick") is True
    assert library.search_book("Jane Air") is False

    assert library._Library__check_availability("War and Peace") is True
    assert library._checkout_book("Moby-Dick") is True
    assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

    assert library.search_book("Moby-Dick") is False
    assert library.return_book("Moby-Dick") is None
    assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
    assert library.search_book("Moby-Dick") is True
    print('Good')
# ------------

class Employee:
    """
    Создайте класс Employee, который имеет следующие методы:
    1. Метод __init__, который устанавливает значения атрибутов name, __position, __hours_worked и __hourly_rate.

    2. Приватный метод calculate_salary, который считает зарплату сотрудника, умножая отработанные часы на часовую оплату.
    Метод должен вернуть посчитанную зарплату.

    3. Защищенный метод _set_position, который принимает название должности и изменяет пользователю значение атрибута
    __position.

    4. Публичный метод get_position, который возвращает атрибут __position.

    5. Публичный метод get_salary, который возвращает результат вызова приватного метода calculate_salary.

    6. публичный метод get_employee_details, который возвращает информацию о работнике в виде следующий строки
    6.1 "Name: {name},
    6.2 Position: {position},
    6.3 Salary: {salary}"
    Здесь значение salary должно рассчитываться при помощи приватного метода calculate_salary.
    """

    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name, self.__position, self.__hours_worked, self.__hourly_rate = name, position, hours_worked, hourly_rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def _set_position(self, name_position):
        self.__position = name_position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"


if __name__ == '__main__':
    employee = Employee("Джеки Чан", 'manager', 20, 40)
    assert employee.name == 'Джеки Чан'
    assert employee._Employee__hours_worked == 20
    assert employee._Employee__hourly_rate == 40
    assert employee._Employee__position == 'manager'
    assert employee.get_position() == 'manager'
    assert employee.get_salary() == 800
    assert employee._Employee__calculate_salary() == 800
    assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
    employee._set_position('Director')
    assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'
    employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
    assert employee_2._Employee__calculate_salary() == 1050
    assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'
    print('Good')
# ------------




