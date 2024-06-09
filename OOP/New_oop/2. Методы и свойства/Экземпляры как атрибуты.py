# ----------------------------------------------- Экземпляры как атрибуты ----------------------------------------------
# -------------------------------  # Божественный объект
# ------------

class ElectricCar:
    """Класс для создания электромобиля"""

    def __init__(self, maker, model, year, battery_size=70):
        self.maker = maker
        self.model = model
        self.year = year
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def describe_car_info(self):
        print(f'{self.maker} {self.model} {self.year}'.title())


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_car_info()
my_tesla.describe_battery()


# Tesla Model S 2016
# This car has a 70-kWh battery.

# -------------------------------
# Божественный объект — анти-паттерн, который довольно часто встречается у ООП разработчиков. Такой объект берет на себя
# слишком много функций и/или хранит в себе практически все данные. В итоге мы имеем непереносимый код, в котором, к
# тому же, сложно разобраться. Также подобный код довольно сложно поддерживать, учитывая, что вся система зависит
# практически только от него.
# -------------------------------

# Разбиваем предыдущий класс на несколько более мелких, выполняющих каждый свою функцию независимо друг от друга.
class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar:
    """Класс для создания электромобиля"""

    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car_info(self):
        print(f'{self.maker} {self.model} {self.year}'.title())


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_car_info()
my_tesla.battery.describe_battery()
print(my_tesla.battery.battery_size)
# Tesla Model S 2016
# This car has a 70-kWh battery.
# 70