# ------------------------------------------- Уровни доступа атрибутов и методов ---------------------------------------
# -------------------------------
# ------------

# Уровни доступа к атрибутам и методам:
# 1. Публичный (public)
# 2. Защищенный (protected)
# 3. Приватный (private)

# -------------------------------
# Публичный доступ:

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


# -------------------------------
# Защищенный (protected) режим:
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


# -------------------------------
# Приватный (private) режим:

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        return self.__name, self.__balance, self.__passport


account1 = BankAccount('Bob', 100000, 45484564654)
print(account1.print_private_data())


# ------------

# Обращаемся к атрибутам через специально созданный метод, напрямую доступ закрыт.
# Например:
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        return self.__name, self.__balance, self.__passport


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


# -------------------------------
# Как получить доступ к приватным атрибутам и методам вне класса:

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

