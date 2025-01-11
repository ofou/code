class DynamicArray:
    """
    A dynamic array class with list-like interface.

    >>> arr = DynamicArray()
    >>> len(arr)
    0
    """

    def __init__(self, capacity=1):
        """
        Initialize the dynamic array with an initial capacity.

        >>> arr = DynamicArray()
        >>> arr.capacity
        1
        >>> len(arr)
        0
        """
        self.capacity = capacity
        self.length = 0
        self.array = [None] * self.capacity

    def __len__(self):
        """
        Return the number of elements.

        >>> arr = DynamicArray()
        >>> arr.append(1)
        >>> len(arr)
        1
        """
        return self.length

    def __getitem__(self, index):
        """
        Retrieve an item by index or slice.

        >>> arr = DynamicArray()
        >>> arr.extend([1, 2, 3])
        >>> arr[0]
        1
        >>> arr[1:3]
        [2, 3]
        """
        if isinstance(index, slice):
            start, stop, step = index.indices(self.length)
            return [self.array[i] for i in range(start, stop, step)]
        if not (0 <= index < self.length):
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __setitem__(self, index, value):
        """
        Set the item(s) at the given index or slice.

        >>> arr = DynamicArray()
        >>> arr.extend([1, 2, 3])
        >>> arr[1] = 10
        >>> arr[1]
        10
        """
        if isinstance(index, slice):
            start, stop, step = index.indices(self.length)
            if hasattr(value, "__iter__"):
                vals = list(value)
                if step == 1 and (stop - start) == len(vals):
                    for i, v in enumerate(vals):
                        self.array[start + i] = v
                else:
                    raise NotImplementedError(
                        "Advanced slice assignment not fully implemented"
                    )
            else:
                raise ValueError("Can only assign an iterable to a slice")
        else:
            if not (0 <= index < self.length):
                raise IndexError("Index out of bounds")
            self.array[index] = value

    def _resize(self, new_capacity):
        """
        Resize the underlying array storage (internal method).

        >>> arr = DynamicArray()
        >>> arr._resize(5)
        >>> arr.capacity
        5
        """
        new_array = [None] * new_capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        """
        Append an item to the end of the array.

        >>> arr = DynamicArray()
        >>> arr.append(99)
        >>> arr[0]
        99
        >>> len(arr)
        1
        """
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1

    def extend(self, iterable):
        """
        Extend the array with items from the given iterable.

        >>> arr = DynamicArray()
        >>> arr.extend([1, 2, 3])
        >>> list(arr)
        [1, 2, 3]
        """
        for item in iterable:
            self.append(item)

    def pop(self, index=None):
        """
        Remove and return item at index, default last.

        >>> arr = DynamicArray()
        >>> arr.extend([1,2,3])
        >>> arr.pop()
        3
        >>> arr.pop(0)
        1
        >>> list(arr)
        [2]
        """
        if self.length == 0:
            raise IndexError("pop from empty list")
        if index is None:
            index = self.length - 1
        if not 0 <= index < self.length:
            raise IndexError("Index out of bounds")
        item = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None
        self.length -= 1
        if self.length <= self.capacity // 4 and self.capacity > 1:
            self._resize(max(self.capacity // 2, 1))
        return item

    def remove(self, value):
        """
        Remove first occurrence of value.

        >>> arr = DynamicArray()
        >>> arr.extend([1,2,3,2])
        >>> arr.remove(2)
        >>> list(arr)
        [1, 3, 2]
        """
        idx = self.find(value)
        if idx == -1:
            raise ValueError("list.remove(x): x not in list")
        self.pop(idx)

    def clear(self):
        """
        Clear the array.

        >>> arr = DynamicArray()
        >>> arr.extend([1,2,3])
        >>> arr.clear()
        >>> len(arr)
        0
        """
        self.capacity = 1
        self.length = 0
        self.array = [None] * self.capacity

    def count(self, value):
        """
        Return the number of occurrences of value.

        >>> arr = DynamicArray()
        >>> arr.extend([2,2,3])
        >>> arr.count(2)
        2
        """
        c = 0
        for i in range(self.length):
            if self.array[i] == value:
                c += 1
        return c

    def index(self, value, start=0, end=None):
        """
        Return the index of the first occurrence of value.

        >>> arr = DynamicArray()
        >>> arr.extend([5,6,7])
        >>> arr.index(6)
        1
        """
        if end is None or end > self.length:
            end = self.length
        for i in range(start, end):
            if self.array[i] == value:
                return i
        raise ValueError("list.index(x): x not in list")

    def __str__(self):
        """
        User-friendly string representation.

        >>> arr = DynamicArray()
        >>> arr.extend([1,2])
        >>> str(arr)
        '[1, 2]'
        """
        elements = [str(self.array[i]) for i in range(self.length)]
        return "[" + ", ".join(elements) + "]"

    def find(self, item):
        """
        Return the index of item or -1 if not found.

        >>> arr = DynamicArray()
        >>> arr.extend([4,5,6])
        >>> arr.find(5)
        1
        >>> arr.find(999)
        -1
        """
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def insert(self, index, item):
        """
        Insert an item at the given index.

        >>> arr = DynamicArray()
        >>> arr.extend([1,2,3])
        >>> arr.insert(1, 99)
        >>> list(arr)
        [1, 99, 2, 3]
        """
        if not 0 <= index <= self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.length += 1

    def reverse(self):
        """
        Reverse the array in-place.

        >>> arr = DynamicArray()
        >>> arr.extend([1,2,3])
        >>> arr.reverse()
        >>> list(arr)
        [3, 2, 1]
        """
        for i in range(self.length // 2):
            self.array[i], self.array[self.length - 1 - i] = (
                self.array[self.length - 1 - i],
                self.array[i],
            )
