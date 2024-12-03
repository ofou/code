import unittest
from array import (
    DynamicArray,
)  # Assume the class is in a file named dynamic_array.py


class TestDynamicArray(unittest.TestCase):

    def setUp(self):
        self.arr = DynamicArray()

    def test_init(self):
        self.assertEqual(len(self.arr), 0)
        self.assertEqual(self.arr.capacity, 1)

    def test_append(self):
        self.arr.append(1)
        self.assertEqual(len(self.arr), 1)
        self.assertEqual(self.arr[0], 1)

        # Test resizing
        for i in range(2, 10):
            self.arr.append(i)
        self.assertEqual(len(self.arr), 9)
        self.assertGreaterEqual(self.arr.capacity, 9)

    def test_insert(self):
        for i in range(5):
            self.arr.append(i)

        self.arr.insert(10, 2)
        self.assertEqual(len(self.arr), 6)
        self.assertEqual(self.arr[2], 10)
        self.assertEqual(list(self.arr), [0, 1, 10, 2, 3, 4])

        # Test insert at beginning
        self.arr.insert(20, 0)
        self.assertEqual(self.arr[0], 20)

        # Test insert at end
        self.arr.insert(30, len(self.arr))
        self.assertEqual(self.arr[-1], 30)

        # Test invalid insert
        with self.assertRaises(IndexError):
            self.arr.insert(40, len(self.arr) + 1)

    def test_remove_at(self):
        for i in range(5):
            self.arr.append(i)

        removed = self.arr.remove_at(2)
        self.assertEqual(removed, 2)
        self.assertEqual(len(self.arr), 4)
        self.assertEqual(list(self.arr), [0, 1, 3, 4])

        # Test remove first
        removed = self.arr.remove_at(0)
        self.assertEqual(removed, 0)
        self.assertEqual(self.arr[0], 1)

        # Test remove last
        removed = self.arr.remove_at(len(self.arr) - 1)
        self.assertEqual(removed, 4)

        # Test invalid remove
        with self.assertRaises(IndexError):
            self.arr.remove_at(len(self.arr))

    def test_find(self):
        for i in range(5):
            self.arr.append(i)

        self.assertEqual(self.arr.find(3), 3)
        self.assertEqual(self.arr.find(10), -1)

    def test_getitem(self):
        for i in range(5):
            self.arr.append(i)

        self.assertEqual(self.arr[2], 2)
        with self.assertRaises(IndexError):
            _ = self.arr[10]

    def test_setitem(self):
        for i in range(5):
            self.arr.append(i)

        self.arr[2] = 10
        self.assertEqual(self.arr[2], 10)
        with self.assertRaises(IndexError):
            self.arr[10] = 5

    def test_iter(self):
        for i in range(5):
            self.arr.append(i)

        self.assertEqual(list(self.arr), [0, 1, 2, 3, 4])

    def test_repr(self):
        for i in range(3):
            self.arr.append(i)

        self.assertEqual(repr(self.arr), "DynamicArray(0, 1, 2)")

    def test_rotate(self):
        for i in range(5):
            self.arr.append(i)

        self.arr.rotate(2)
        self.assertEqual(list(self.arr), [3, 4, 0, 1, 2])

        # Test rotate with k > length
        self.arr.rotate(7)
        self.assertEqual(list(self.arr), [1, 2, 3, 4, 0])

    def test_is_sorted(self):
        self.assertTrue(self.arr.is_sorted())

        for i in range(5):
            self.arr.append(i)
        self.assertTrue(self.arr.is_sorted())

        self.arr[2] = 10
        self.assertFalse(self.arr.is_sorted())

    def test_binary_search(self):
        for i in range(0, 10, 2):
            self.arr.append(i)

        self.assertEqual(self.arr.binary_search(6), 3)
        self.assertEqual(self.arr.binary_search(5), -1)

    def test_remove_duplicates(self):
        for i in [1, 2, 2, 3, 4, 4, 4, 5]:
            self.arr.append(i)

        self.arr.remove_duplicates()
        self.assertEqual(list(self.arr), [1, 2, 3, 4, 5])

    def test_resize(self):
        # Start with a larger initial capacity to allow for shrinking
        self.arr = DynamicArray(4)  # Start with capacity 4 instead of 1
        initial_capacity = self.arr.capacity

        # Test growing
        for i in range(initial_capacity + 1):
            self.arr.append(i)
        self.assertGreater(self.arr.capacity, initial_capacity)

        # Test shrinking
        while len(self.arr) > initial_capacity // 4:
            self.arr.remove_at(0)
        self.assertLess(self.arr.capacity, initial_capacity)


if __name__ == "__main__":
    unittest.main()
