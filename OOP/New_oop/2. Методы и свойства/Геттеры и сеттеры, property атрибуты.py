# --------------------------------------- Геттеры и сеттеры, property атрибуты -----------------------------------------
# -------------------------------
# ------------

# Property. getter-метод и setter-метод

# Функция property:
# Property позволяет поместить в свойство сразу get, set, del, doc:
property(fget=None, fset=None, fdel=None, doc=None)


# property  — это функция, которая позволяет превращать атрибуты класса в свойства или управляемые атрибуты.

# Возвращаемое значение property — это сам управляемый атрибут. Когда вы обращаетесь к управляемому атрибуту,
# как в obj.attr, тогда Python автоматически вызывает fget(). Когда вы присваиваете атрибуту новое значение,
# как в obj.attr = value, тогда Python вызывает fset(), используя входное значение в качестве аргумента. Наконец,
# если вы запустите оператор del obj.attr, то Python автоматически вызовет fdel().

class Person:
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        print("Get name")
        return self._name

    def _set_name(self, value):
        print("Set name")
        self._name = value

    def _del_name(self):
        print("Delete name")
        del self._name

    name = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="The name property."
    )


if __name__ == '__main__':
    person = Person('Jack')
    person.name  # Get name

    person.name = 'Jamal'
    person.name  # Set name

    del person.name  # Delete name

help(person)


# Help on Person in module __main__ object:
# class Person(builtins.object)
#  |  Person(name)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object
#  |
#  |  name
#  |      The name property.

# -------------------------------

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self) -> int:
        return self.__balance

    def set_balance(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("incorrect balance")
        self.__balance = value

    def delete_balance(self) -> None:
        del self.__balance

    bal_prop = property(get_balance, set_balance, delete_balance, "This is 'value' property.")


b = BankAccount('Vladislav Sereda', 100)

print(b.bal_prop)  # 100

b.bal_prop = 'Hello!'
print(b.bal_prop)  # raise ValueError("incorrect balance") ValueError: incorrect balance

b.bal_prop = 750
print(b.bal_prop)  # 750

print(b.__dict__)  # {'name': 'Vladislav Sereda', '_BankAccount__balance': 750}


# -------------------------------

class UserMail:
    """
    Создайте класс UserMail, у которого есть:
    1. конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. Их необходимо сохранить в экземпляр, как
    атрибуты login и __email (обратите внимание, приватный атрибут).
    2. Метод геттер get_email, который возвращает приватный атрибут __email.
    3. Метод сеттер set_email, который принимает в виде строки новую почту. Метод должен проверять, что в новой почте есть
    только один символ @ и после него есть точка. Если данные условия выполняются, новая почта сохраняется в атрибут
    __email, в противном случае выведите сообщение "ErrorMail:<почта>".
    """

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if len(result := list(filter(lambda x: x in ['@', '.'], value))) == 2 and result[0] == '@':
            self.__email = value
        else:
            print(f"ErrorMail:{value}")

    email = property(fget=get_email, fset=set_email)


if __name__ == "__main__":
    jim = UserMail("aka47", 'hello@com.org')
    assert jim.login == "aka47"
    assert jim._UserMail__email == "hello@com.org"
    assert isinstance(jim, UserMail)
    assert isinstance(type(jim).email, property), 'Вы не создали property email'

    jim.email = [1, 2, 3]
    jim.email = 'hello@@re.ee'
    jim.email = 'hello@re.w3'
    assert jim.email == 'hello@re.w3'

    k = UserMail('belosnezhka', 'prince@wait.you')
    assert k.email == 'prince@wait.you'
    assert k.login == 'belosnezhka'
    assert isinstance(k, UserMail)

    k.email = {1, 2, 3}
    k.email = 'prince@still@.wait'
    k.email = 'prince@stillwait'
    k.email = 'prince@still.wait'
    assert k.get_email() == 'prince@still.wait'
    k.email = 'pri.nce@stillwait'
    assert k.email == 'prince@still.wait'
