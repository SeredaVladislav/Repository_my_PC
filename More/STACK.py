class Stack:
    """
    Реализовать свой стек (stack) — это упорядоченная коллекция элементов, организованная по принципу LIFO
    (англ. last in — first out, «последним пришёл — первым вышел»).
    """

    def __init__(self) -> None:
        self.values: list = []

    def push(self, item) -> None:
        self.values.append(item)

    def pop(self) -> int or None:
        if self.values:
            element = self.values.pop(-1)
            return element
        print("Empty Stack")

    def peek(self) -> int or None:
        if self.values:
            return self.values[-1]
        print("Empty Stack")

    def is_empty(self) -> bool:
        return self.values == []

    def size(self) -> int:
        return len(self.values)


if __name__ == '__main__':
    s = Stack()
    assert s.values == []
    assert isinstance(s, Stack)

    s.peek()
    assert s.is_empty() is True
    s.push('cat')
    assert s.size() == 1
    assert s.peek() == 'cat'

    s.push('dog')
    assert s.size() == 2
    assert s.peek() == 'dog'

    s.push(True)
    assert s.size() == 3
    assert s.is_empty() is False

    s.push(777)
    assert s.size() == 4

    assert s.pop() == 777
    assert s.size() == 3

    assert s.pop() is True
    assert s.size() == 2

    s.push(123)
    s.push(123456)
    assert s.peek() == 123456
    assert s.size() == 4

    assert s.pop() == 123456
    assert s.pop() == 123
    assert s.pop() == 'dog'
    assert s.is_empty() is False
    assert s.pop() == 'cat'
    assert s.is_empty() is True

    d = Stack()
    assert d.peek() is None
    assert d.pop() is None
    d.push('hello')
    assert d.size() == 1
    d.push('world')
    assert d.size() == 2
    assert d.peek() == 'world'
    assert d.pop() == 'world'
    assert d.peek() == 'hello'