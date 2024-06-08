# ---------------------------------------------- Наследование ----------------------------------------------------------

# Идея наследования класса состоит в том, что новый класс создается не на «пустом месте», а на основе уже существующего.
# В результате наследования все поля и функции из базового класса неявным образом «наследуются» в производном классе.

import datetime


class Product:
    max_quantity = 100_000

    def __init__(self, name, category, quantity_in_stock):
        self.name_ = name
        self.category_ = category
        self.quantity_in_stock_ = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock_ > 0 else False


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)

print(eggs.is_available())


# Мы видим, что мы создавали объект eggs как экземпляр класса Food, но при этом ему доступны как атрибуты
# родительского класса (max_quantity), так и его методы (is_available).
# Фактически произошло ещё более интересное: для создания экземпляра класса Food мы использовали
# конструктор его родительского класса Product.


# Прежде чем пойти дальше, давайте изучим одну полезную конструкцию: if __name__ == "__main__"
# Давайте разберем на примере и создадим два файла: _1_файл.py и _2_файл.py.

# ________________ файл _1_файл.py
class MyClass():
    def f(self):
        return 155


mc2 = MyClass()
print("Это для теста", mc2.f())

if __name__ == "__main__":
    mc = MyClass()
    print("Тест", mc.f())

# ________________ файл _2_файл.py

from myclass import MyClass  # импортируем Класс из другого файла

if __name__ == "__main__":
    m = MyClass()
    print("Работает!:", m._())


# Это для теста 155
# Работает! 155


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp_ = timestamp
        self.type_ = event_type
        self.session_id_ = session_id

    def init_from_dict(self, event_dict):
        self.timestamp_ = event_dict.get("timestamp")
        self.type_ = event_dict.get("type")
        self.session_id_ = event_dict.get("session_id")

    def show_description(self):
        print("Общее событие.")


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("Это событие означает, что кто-то просмотрел элемент.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)


# Переопределили конструктор класса. Теперь мы используем не родительский, а свой, и передаём в него другой набор
# аргументов. Так у нас получился кастомизированный набор атрибутов: у родительского класса нет атрибута number_of_views

# Переопределили значение атрибута type с помощью атрибута класса. Теперь при вызове type от экземпляра нашего
# дочернего класса мы получим значение атрибута type нашего класса ItemViewEvent.

# Переопределили работу метода show_description: теперь он показывает более специфичное для класса описание.


class Room1:
    def get_room(self):
        print('room1')


class Room2:
    def get_room(self):
        print('room2')

    def get_room2(self):
        print('room2 for flat')


class Kitchen:
    def get_kitchen(self):
        print('kitchen')


class Flat(Kitchen, Room1, Room2):
    ...


f = Flat()
f.get_kitchen()
f.get_room()
f.get_room2()


# Класс Flat наследует классы отдельных комнат в следующем порядке: Kitchen, Room1, Room2.
# Это значит, что поиск методов при их вызове (_.get_kitchen() и др.) сначала будет осуществляться в
# классе Kitchen, затем, если метод не найден, в классе Room1, и только затем Room2. Это хорошо видно на
# примере вызова метода get_room().

class Room:
    def get_room(self):
        print('room')


class Room1(Room):
    def get_room(self):
        print('room1')


class Room2(Room):
    def get_room(self):
        print('room2')


class Flat(Room1, Room2):
    ...


print(Flat.mro())  # метод класса, который показывает порядок наследования

f = Flat()
f.get_room()
