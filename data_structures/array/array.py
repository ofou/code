class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.length = 0
        self.array = [None] * self.capacity

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if -self.length <= index < self.length:
            # Convert negative index to positive
            if index < 0:
                index += self.length
            return self.array[index]
        raise IndexError("Index out of bounds")

    def __setitem__(self, index, value):
        if not 0 <= index < self.length:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(min(self.length, new_capacity)):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        self.length = min(self.length, new_capacity)

    def append(self, item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1

    def insert(self, item, index):
        if not 0 <= index <= self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.length += 1

    def remove_at(self, index):
        if not 0 <= index < self.length:
            raise IndexError("Index out of bounds")
        item = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None
        self.length -= 1
        # Check if we need to shrink the array
        if self.length <= self.capacity // 4 and self.capacity > 1:
            self._resize(max(self.capacity // 2, 1))  # Ensure capacity doesn't become 0

        return item

    def find(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < self.length:
            item = self.array[self._iter_index]
            self._iter_index += 1
            return item
        raise StopIteration

    def __repr__(self):
        return f"DynamicArray({', '.join(repr(self.array[i]) for i in range(self.length))})"

    def rotate(self, k):
        if self.length == 0:
            return
        k = k % self.length  # Normalize k
        self._reverse(0, self.length - 1)
        self._reverse(0, k - 1)
        self._reverse(k, self.length - 1)

    def _reverse(self, start, end):
        while start < end:
            self.array[start], self.array[end] = self.array[end], self.array[start]
            start += 1
            end -= 1

    def is_sorted(self):
        return all(self.array[i] <= self.array[i + 1] for i in range(self.length - 1))

    def binary_search(self, item):
        left, right = 0, self.length - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == item:
                return mid
            elif self.array[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Item not found

    def remove_duplicates(self):
        if self.length <= 1:
            return

        write_index = 1
        for read_index in range(1, self.length):
            if self.array[read_index] != self.array[write_index - 1]:
                self.array[write_index] = self.array[read_index]
                write_index += 1

        for i in range(write_index, self.length):
            self.array[i] = None

        self.length = write_index


# Example usage and testing
if __name__ == "__main__":
    arr = DynamicArray()

    # Test append and print
    for i in range(10):
        arr.append(i)
    print(f"Array after appending 0-9: {arr}")

    # Test insert
    arr.insert(99, 5)
    print(f"Array after inserting 99 at index 5: {arr}")

    # Test remove_at
    removed = arr.remove_at(3)
    print(f"Removed {removed} from index 3. Array is now: {arr}")

    # Test find
    index = arr.find(99)
    print(f"99 found at index: {index}")

    # Test __getitem__ and __setitem__
    print(f"Element at index 5: {arr[5]}")
    arr[5] = 100
    print(f"After changing element at index 5 to 100: {arr}")

    # Test iteration
    print("Iterating over array:")
    for item in arr:
        print(item, end=" ")
    print()

    # Test rotate
    arr.rotate(3)
    print(f"Array after rotating by 3 positions: {arr}")

    # Test is_sorted
    print(f"Is the array sorted? {arr.is_sorted()}")

    # Test binary_search
    sorted_arr = DynamicArray()
    for i in range(10):
        sorted_arr.append(i * 2)
    print(f"Sorted array: {sorted_arr}")
    print(f"Binary search for 6: {sorted_arr.binary_search(6)}")

    # Test remove_duplicates
    dup_arr = DynamicArray()
    for i in [1, 2, 2, 3, 4, 4, 4, 5]:
        dup_arr.append(i)
    print(f"Array with duplicates: {dup_arr}")
    dup_arr.remove_duplicates()
    print(f"Array after removing duplicates: {dup_arr}")

    # Test multiple iterations
    print("Testing multiple iterations:")
    iter_arr = DynamicArray()
    for i in range(5):
        iter_arr.append(i)

    print("First iteration:")
    for item in iter_arr:
        print(item, end=" ")
    print()

    print("Second iteration:")
    for item in iter_arr:
        print(item, end=" ")
    print()

    print(f"Original array: {iter_arr}")
