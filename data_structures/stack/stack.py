class Stack:

    def __init__(self, max_size=None):
        self._items = []
        self._max_size = max_size

    def push(self, item):
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise OverflowError("Stack has reached its maximum size")
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()

    def copy(self):
        new_stack = Stack(max_size=self._max_size)
        new_stack._items = self._items.copy()
        return new_stack

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return NotImplemented
        return self._items == other._items and self._max_size == other._max_size

    def __iter__(self):
        return reversed(self._items)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(size={self.size()}, max_size={self._max_size})"
        )

    def __bool__(self):
        return bool(self._items)
