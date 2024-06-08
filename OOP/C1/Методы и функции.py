# ---------------------------------------------- Методы и функции ------------------------------------------------------

# Метод — это всего лишь функция, реализованная внутри класса, и первым аргументом принимающая self

class Product:
    def __init__(self, name, category, quantity_in_stock):  # Конструктор-метод Класса
        self.name = name  # экземпляр Класса
        self.category = category  # экземпляр Класса
        self.quantity_in_stock = quantity_in_stock  # экземпляр Класса

    def is_available(self):  # Функции-методы (из-за self)
        return True if self.quantity_in_stock > 0 else False


eggs = Product("eggs", "food", 1)  # вызов метода на исполнение (передача аргументов)
print(eggs.is_available())  # вывод в консоль метода is_available


# Разница между методом и функцией только в том, что метод вызывается от конкретного объекта и реализован внутри класса.

class Event:  # Класс
    def __init__(self, timestamp, event_type, session_id):  # Конструктор-метод Класса
        self.timestamp = timestamp  # экземпляр Класса
        self.type = event_type  # экземпляр Класса
        self.session_id = session_id  # экземпляр Класса


events = [
    {
        "timestamp": 1554583508000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]  # Список словарей

for event in events:  # цикл для перебора списка
    event_obj = Event(timestamp=event.get("timestamp"),  # присваивание Классу переменной
                      event_type=event.get("type"),  # Атрибуты Конструктора с именами ключей словаря
                      session_id=event.get("session_id"))  # Атрибуты Конструктора с именами ключей словаря
    print(event_obj.timestamp)  # Вывод переменной с нужным атрибутом Конструктора

# Здесь мы использовали метод словаря .get(), который возвращает значение ключа и не вызывает ошибку,
# если такого ключа в словаре нет.

events = [
    {
        "timestamp": 1554583508000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]  # Список словарей


class Event:  # Класс
    def __init__(self, timestamp=0, event_type="", session_id=""):  # Конструктор-метод Класса
        self.timestamp = timestamp  # экземпляр Класса
        self.type = event_type  # экземпляр Класса
        self.session_id = session_id  # экземпляр Класса

    def init_from_dict(self, event_dict):  # Метод с аргументом
        self.timestamp = event_dict.get("timestamp")  # экземпляры Конструктора принимают аргумент Метода с Ключом
        self.type = event_dict.get("type")  # экземпляры Конструктора принимают аргумент Метода с Ключом
        self.session_id = event_dict.get("session_id")  # экземпляры Конструктора принимают аргумент Метода с Ключом


for event in events:  # цикл перебора списка словарей
    event_obj = Event()  # присваивание Класса в переменную
    event_obj.init_from_dict(event)  # к переменной используем метод с указанием аргумента в роли переменной цикла
    print(event_obj.timestamp)  # Вывод переменной с методом экземпляра Метода

# Стандартные типы данных Python также предоставляют готовый набор методов для работы с ними.
# Например, у строки есть метод .split(), который мы уже использовали — и это именно метод в полноценном
# смысле: где-то внутри Python определён класс строк и их метод.

