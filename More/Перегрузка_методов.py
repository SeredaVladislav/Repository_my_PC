class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


calc = Calculator()

# Первая версия метода add будет переопределена второй версией
# Метод add с двумя аргументами не будет доступен
result1 = calc.add(2, 3, 4)  # вызывается вторая версия метода add
result2 = calc.add(2, 3)  # вызывается первая версия метода add

print(result1)  # Вывод: 9
print(result2)  # Ошибка! Такой метод не существует




# исправление перегруженности:
class Calculator:
    def add(self, x, y=0, z=0):
        return x + y + z


calc = Calculator()

result1 = calc.add(2, 3, 4)  # Вызывается версия с тремя аргументами
result2 = calc.add(2, 3)  # Вызывается версия с двумя аргументами (y и example_list_2 принимают значения по умолчанию)

print(result1)  # Вывод: 9
print(result2)  # Вывод: 5
