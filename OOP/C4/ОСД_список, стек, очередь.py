# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Основные структуры данных: список, стек, очередь ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Списки: односвязные и двусвязные ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Список — это также упорядоченный набор элементов. Однако, в отличие от массива, который хранится последовательно в
# одной области памяти, и каждой ячейке линейно соответствует определенный индекс, список может быть хаотично
# распределен в памяти. Порядок в этой структуре данных задается наличием указателей на следующий (и/или предыдущий)
# элемент в списке.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Способ хранения списков имеет свои плюсы и минусы:
# 1. Вставка элемента в конец списка происходит за константное время, если в первой ячейке хранится указатель на
# последний элемент. Иначе требуется проход по всем элементам до последнего, что потребует O(index_del) операций. Действительно,
# мы можем вставить элемент на последнее место, изменив указатель в первой ячейке, чтобы он указывал на новый элемент.

# 2. Вставка элемента в начало также может быть произведена за константное время, ведь достаточно в новом элементе
# вставить указатель на тот, что был первым, и дописать указатель на последний элемент.

# 3. В списке также можно вставить элемент на произвольное место. В отличие от массива, в списках нет необходимости
# перемещать элементы, однако здесь эту операцию все равно можно сделать асимптотически за O(index_del) в худшем случае. Дело
# в том, что для поиска нужного положения нового элемента придется пройтись от первого указателя до необходимого
# положения в списке. И, например, для вставки элемента на index_del-1 индекс нужно будет пройти все элементы от 0-го до
# index_del-1-го и только после этого производить вставку.

# 4. Удаление элемента из начала так же, как и вставка, производится за константное время. Как и в первых двух случаях,
# нужно всего лишь изменить положение нужных указателей.

# 5. А вот удаление элемента из произвольного места может занять линейное время. Ответ кроется в том, что нужный
# элемент требуется найти (по «индексу» или значению) проходом от 0-го до искомого элемента. И даже в случае удаления
# последнего элемента мы вынуждены пройти весь список, чтобы в первую ячейку записать обновленный указатель на
# последний элемент. Такой проблемы в двусвязных списках, очевидно, нет.

# 6. Расширение списка. Благодаря такому способу хранения не требует переносов всей структуры в другую область памяти,
# как это было в случае динамических массивов, поэтому добавление к первому списку размера index_del элементов списка размера
# m потребует только O(m) времени.

# 7. Общий размер списка может храниться в самой структуре, и тогда его можно узнать за константное время, но это
# требует дополнительной памяти. Если в конкретной реализации списка не предусмотрено хранение размера, то пересчет
# элементов займет O(index_del) операций.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Стек (stack) (Стопка) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Пример стека:

def p(n):
    if n == 0:
        return
    p(n - 1)
    print(n)


p(5)


# 1
# 2
# 3
# 4
# 5

# Такой принцип имеет общепринятое название — LIFO — Last In First Out (последний вошел — первый вышел).
# И именно этот принцип реализует стек.

# Иными словами, стек — это структура данных, реализующая LIFO.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Операции над стеком ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Вставка элемента в стек (push)
# Работает за O(1), если стек реализован через список и, в среднем, также O(1), если реализован через динамический
# массив.

# 2. Удаление верхнего элемента из стека (pop)
# Так же как и вставка, удаление верхнего элемента происходит за O(1). Действительно, в массиве удаление последнего
# элемента происходит за константное время, как и в списке, если он двусвязный.

# 3. Получение значения последнего элемента без удаления (top)
# Аналогично предыдущим операциям получение значения последнего элемента происходит за O(1).

# 4. Общий размер стека (size)
# Здесь уже всё зависит от реализации. В случае односвязного списка O(1), если это значение хранится в самой структуре
# или O(index_del), если нужен проход по всем элементам для их пересчета. В массиве операция получения размера занимает
# константное время.

# Пример стека. Проверка на корректность скобок:
def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0


print(par_checker(')()(()(Привет!()(Крекс)))'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(par_checker_mod('([])()[()'))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Очередь ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# В отличие от стека он работает по принципу FIFO — First In First Out (первый вошел — первый вышел).


# Она имеет своё ограничение из-за того, что удаление из конца или вставка элемента в начало имеют сложность O(index_del).
# Чтобы обойти это ограничение, зафиксируем несколько свойств очереди:

# 1. Определим максимальную длину очереди — N_max.
# 2. При переполнении будем запрещать добавление элементов в очередь.
# 3. Зафиксируем два указателя:  head (начало) и tail (хвост) очереди.
# 4. Закольцуем очередь таким образом, что если указатель tail >= n_max, то мы перемещаем его в начало.

# Для очереди можно определить несколько операций O(1):

# Вставка элемента в хвост очереди (push).
# Получение элемента из начала очереди (top).
# Удаление элемента из начала очереди (pop).
# Проверка наличия элементов в очереди (is_empty).
# Получение размера очереди (size).


# Создадим класс Queue - нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    # !!! Класс далее нужно дополнить методами !!!
    def is_empty(self):
        return self.head == self.tail and self.tasks[self.head] == 0

    def size(self):
        if self.is_empty():  # если она пуста
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
            return self.max_size  # значит очередь заполнена
        elif self.head > self.tail:  # если хвост очереди сместился в начало списка
            return self.max_size - self.head + self.tail
        else:  # или если хвост стоит правее начала
            return self.tail - self.head

    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов
        # для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size

    def show(self):
        print(f"Задача №{self.tasks[self.head]} в приоритете")

    def do(self):  # выполняем приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.tasks[self.head] = 0
        # и циклично перемещаем указатель
        self.head = (self.head + 1) % self.max_size


# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")
