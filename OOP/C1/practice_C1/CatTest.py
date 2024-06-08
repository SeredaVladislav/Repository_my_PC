class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


# Наследование:

class Cat:
    def __init__(self, name):
        self.name = name


class Dog(Cat):
    def __init__(self, name, gender, age):
        super().__init__(name)  # Метод super() переопределение методов Родительского Класса
        self.gender = gender
        self.age = age

    def get_pet(self):
        return f'{self.name} {self.age}'


dog_1 = Dog("Felix", "boy", 2)
print(dog_1.get_pet())
