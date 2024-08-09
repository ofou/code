import unittest
from .stack import Stack
import sys
import time


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_pop_large_number_of_items(self):
        """Test pushing and popping a large number of items."""
        num_items = 1000000
        for i in range(num_items):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), num_items)
        for i in reversed(range(num_items)):
            self.assertEqual(self.stack.pop(), i)
        self.assertTrue(self.stack.is_empty())

    def test_push_pop_performance(self):
        """Test the performance of push and pop operations."""
        num_operations = 100000
        start_time = time.time()
        for i in range(num_operations):
            self.stack.push(i)
        for _ in range(num_operations):
            self.stack.pop()
        end_time = time.time()
        self.assertLess(
            end_time - start_time, 1.0
        )  # Assert that 100,000 push/pop operations take less than 1 second

    def test_memory_usage(self):
        """Test that the stack doesn't use excessive memory."""
        initial_memory = sys.getsizeof(self.stack)
        for i in range(1000):
            self.stack.push(i)
        final_memory = sys.getsizeof(self.stack)
        self.assertLess(
            final_memory - initial_memory, 10000
        )  # Assert that 1000 pushes use less than 10KB additional memory

    def test_push_different_types(self):
        """Test pushing items of different types onto the stack."""
        items = [1, "string", [1, 2, 3], {"key": "value"}, (1, 2), set([1, 2, 3])]
        for item in items:
            self.stack.push(item)
        for item in reversed(items):
            self.assertEqual(self.stack.pop(), item)

    def test_clear_stack(self):
        """Test clearing the stack."""
        for i in range(10):
            self.stack.push(i)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_push_pop_alternating(self):
        """Test alternating push and pop operations."""
        for i in range(100):
            self.stack.push(i)
            if i % 2 == 0:
                self.assertEqual(self.stack.pop(), i)
        self.assertEqual(self.stack.size(), 50)

    def test_stack_with_none_values(self):
        """Test stack operations with None values."""
        self.stack.push(None)
        self.assertEqual(self.stack.size(), 1)
        self.assertIsNone(self.stack.peek())
        self.assertIsNone(self.stack.pop())

    def test_stack_representation(self):
        """Test the string representation of the stack."""
        for i in range(5):
            self.stack.push(i)
        self.assertIn("Stack", str(self.stack))
        self.assertIn("5", str(self.stack))  # Size should be mentioned

    def test_stack_copy(self):
        """Test creating a copy of the stack."""
        for i in range(5):
            self.stack.push(i)
        stack_copy = self.stack.copy()
        self.assertEqual(self.stack.size(), stack_copy.size())
        while not self.stack.is_empty():
            self.assertEqual(self.stack.pop(), stack_copy.pop())

    def test_stack_comparison(self):
        """Test comparing two stacks."""
        stack1 = Stack()
        stack2 = Stack()
        for i in range(5):
            stack1.push(i)
            stack2.push(i)
        self.assertEqual(stack1, stack2)
        stack1.push(5)
        self.assertNotEqual(stack1, stack2)

    def test_stack_iterable(self):
        """Test if the stack is iterable."""
        items = list(range(5))
        for item in items:
            self.stack.push(item)
        self.assertEqual(list(self.stack), list(reversed(items)))

    def test_stack_max_size(self):
        """Test stack with a maximum size limit."""
        max_size = 5
        limited_stack = Stack(max_size=max_size)
        for i in range(10):
            if i < max_size:
                limited_stack.push(i)
            else:
                with self.assertRaises(OverflowError):
                    limited_stack.push(i)
        self.assertEqual(limited_stack.size(), max_size)


if __name__ == "__main__":
    unittest.main()
