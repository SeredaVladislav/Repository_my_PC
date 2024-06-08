class Room1:
    def get_room(self):  # Одинаковые методы разных Классов
        print('room1')


class Room2:
    def get_room(self):  # Одинаковые методы разных Классов
        print('room2')

    def get_room2(self):
        print('room2 for flat')


class Kitchen:
    def get_kitchen(self):
        print('kitchen')


class Flat(Kitchen, Room1, Room2):  # Дочерний Класс принимает Наследование для 3 Классов
    # (Очередность принимаемых аргументов будет влиять на приоритетность поиска методов)
    ...


f = Flat()  # Экземпляр Класса
f.get_kitchen()
f.get_room()  # Будет использован Метод из Класса Room1, так как в принимаемых Аргументах Класса Flat приоритет
f.get_room2()


# ----------------------------------------------------------------------------------------------------------------------

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
