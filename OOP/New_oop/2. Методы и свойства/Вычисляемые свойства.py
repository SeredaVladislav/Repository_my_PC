# Смысл Вычисляемых свойств в Кэшировании уже вычисленных значений, а не повторное их вычисление.

# Пример:
import time


class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):  # В случае изменения значения атрибута, присваиваем значение None атрибуту __area.
        self.__side = value
        self.__area = None

    @property
    def area(self):  # Кэширование, если атрибут __area не None, иначе новый подсчет.
        if self.__area is None:
            print('Calculate area...')
            time.sleep(0.5)
            self.__area = self.side ** 2
        return self.__area


sq = Square(4)
print(sq.area)
print(sq.area)


# --------------------------------------------
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        return f"{self.day:02}/{self.month:02}/{self.year:04}"

    @property
    def usa_date(self):
        return f"{self.month:02}-{self.day:02}-{self.year:04}"


if __name__ == '__main__':
    d1 = Date(5, 10, 2001)
    assert isinstance(d1, Date)
    assert d1.date == '05/10/2001'
    assert d1.usa_date == '10-05-2001'
    assert isinstance(type(d1).date, property), 'Вы не создали property date'
    print(d1.date, d1.usa_date)

    d2 = Date(15, 3, 999)
    assert isinstance(d2, Date)
    assert d2.date == '15/03/0999'
    assert d2.usa_date == '03-15-0999'
    assert isinstance(type(d2).date, property), 'Вы не создали property date'
    print(d2.date, d2.usa_date)

    d3 = Date(3, 5, 3)
    assert d3.date == '03/05/0003'
    assert d3.usa_date == '05-03-0003'
    print(d3.date, d3.usa_date)


# --------------------------------------------
class Password:
    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        result_pass = None
        if len(self.password) >= 12:
            result_pass = "Strong"
        elif len(self.password) < 8:
            result_pass = "Weak"
        else:
            result_pass = "Medium"

        return result_pass


if __name__ == '__main__':
    pass_1 = Password("Alligator34")
    assert pass_1.password == "Alligator34"
    assert pass_1.strength == "Medium"
    assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

    pass_2 = Password("Alligator345678")
    assert pass_2.password == "Alligator345678"
    assert pass_2.strength == "Strong"
    pass_1.password = "123"
    assert pass_1.strength == "Weak"
    assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

    pass_3 = Password("345678")
    assert pass_3.strength == "Weak"
    print('Good')
    assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'
