# --------------------------------------------- Атрибуты экземпляра класса ---------------------------------------------
# -------------------------------
# ------------

# instance_name.attribute_name
# где instance_name — экземпляра класса, к которому обращаемся, а attribute_name — имя атрибута. Например:

class Person:
    name = 'Ivan'
    age = 30


man = Person()  # Создаём ЭК и связываем его с переменной man
print(man.age)  # 30
man.money = 100  # Создаём в ЭК атрибут money со значением 100
print(man.money)  # 100
man.money = 250  # Изменяем текущее значение атрибута money в ЭК man на 250
print(man.money)  # 250
delattr(man, 'money')  # Удаляем атрибут money из ЭК
print(hasattr(man, 'money'))  # False


# ------------
# Экземпляра класса имеют только ссылку на атрибуты класса, но не имеют их:
class Person:
    name = 'Ivan'
    age = 30


man = Person()
print(man.__dict__)  # {}
print('-------')
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Ivan', 'age': 30,


# '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None}

# ------------
# При изменении атрибута из-под экземпляра класса, произойдет запись нового атрибута в экземпляр класса, но не в класс:
class Person:
    name = 'Ivan'
    age = 30


man = Person()
print(man.__dict__)  # {}
man.name = 'Alex'
print(man.__dict__)  # {'name': 'Alex'}

# ------------
# Атрибуты двух ЭК независимы друг от друга, и все изменения касаются непосредственно тех ЭК, где они проводятся.
# В то же время, операции с атрибутами класса отражаются по всей цепочке от класса до экземпляра класса, кроме тех
# атрибутов, которые уже принадлежат ЭК, что указывает нам на различие пространства имён этих объектов.

# Если в классе и ЭК находятся аргументы с одинаковыми именами и разными значениями, то в случае удаления одноимённого
# аргумента из ЭК, при обращении к аргументу ЭК будет выводиться аргумент из самого класса.

# --------------------------------------------------- Задачи -----------------------------------------------------------
"""
    Ниже определен пустой класс SuperHero. 
    Ваша задача: создать два ЭК и сохранить их в переменные batman и superman.
    
    Для ЭК, хранящегося в переменной batman, необходимо создать:
    1. атрибут can_fly со значением False
    2. атрибут damage со значением 175
    
    Для ЭК, хранящегося в переменной superman, необходимо создать:
    1. атрибут can_fly со значением True
    2. атрибут damage со значением 285
    3. атрибут alter_ego со значением 'Кларк Кент'
"""


class SuperHero:
    pass


batman = SuperHero()
superman = SuperHero()

batman.can_fly = False
batman.damage = 175

superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'
# ------------


"""
    Имеется пустой класс Config. 
    Ваша задача написать функцию create_instance, которая принимает на вход положительное число N. 
    Функция должна создать ЭК, создать у него N атрибутов и вернуть в качестве ответа полученный ЭК.
    Что касается атрибутов, они должны называться определенным образом и иметь определенное значение. 
    В общем виде это можно записать так:
    attribute<n> = "value<n>", где n — порядковый номер атрибута. Значение атрибута — строковый тип.
"""


class Config:
    pass


def create_instance(n: int) -> Config:
    obj = Config()
    for i in range(1, n + 1):
        setattr(obj, f'attribute{i}', f'value{i}')

    return obj


# Ниже расположены проверки для функции create_instance

config_2 = create_instance(2)
assert isinstance(config_2, Config)
assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}

config_4 = create_instance(4)
assert isinstance(config_4, Config)
assert config_4.__dict__ == {'attribute1': 'value1',
                             'attribute2': 'value2',
                             'attribute3': 'value3',
                             'attribute4': 'value4'}

config_7 = create_instance(7)
assert isinstance(config_7, Config)
assert config_7.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
                             'attribute3': 'value3', 'attribute4': 'value4',
                             'attribute5': 'value5',
                             'attribute6': 'value6',
                             'attribute7': 'value7'}

config_10 = create_instance(10)
assert isinstance(config_10, Config)
assert config_10.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
                              'attribute3': 'value3', 'attribute4': 'value4',
                              'attribute5': 'value5', 'attribute6': 'value6',
                              'attribute7': 'value7', 'attribute8': 'value8',
                              'attribute9': 'value9', 'attribute10': 'value10'}

print('good')
# ------------
