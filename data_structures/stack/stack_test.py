import unittest
from stack import Stack


class Test_Stack(unittest.TestCase):

    def test_is_empty(self: any) -> None:
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek(), 2)

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)


if __name__ == '__main__':
    unittest.main()
