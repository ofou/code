import unittest
from .singly_linked import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()

    def test_empty_list_operations(self):
        self.assertIsNone(self.list.head)
        self.assertEqual(self.list.get_count(), 0)
        self.assertFalse(self.list.search_item(5))
        self.list.insert_before_item(5, 10)  # Should not raise an error
        self.list.insert_after_item(5, 10)  # Should not raise an error

    def test_insert_at_beginning(self):
        self.list.insert_at_beginning(5)
        self.assertEqual(self.list.head.data, 5)
        self.list.insert_at_beginning(10)
        self.assertEqual(self.list.head.data, 10)
        self.assertEqual(self.list.head.next.data, 5)

    def test_insert_at_end(self):
        self.list.insert_at_end(5)
        self.assertEqual(self.list.head.data, 5)
        self.list.insert_at_end(10)
        self.assertEqual(self.list.head.data, 5)
        self.assertEqual(self.list.head.next.data, 10)

    def test_insert_after_item(self):
        self.list.insert_at_end(5)
        self.list.insert_at_end(10)
        self.list.insert_after_item(5, 7)
        self.assertEqual(self.list.head.next.data, 7)
        self.assertEqual(self.list.head.next.next.data, 10)

    def test_insert_before_item(self):
        self.list.insert_at_end(5)
        self.list.insert_at_end(10)
        self.list.insert_before_item(10, 7)
        self.assertEqual(self.list.head.next.data, 7)
        self.assertEqual(self.list.head.next.next.data, 10)

    def test_get_count(self):
        self.assertEqual(self.list.get_count(), 0)
        self.list.insert_at_end(5)
        self.assertEqual(self.list.get_count(), 1)
        self.list.insert_at_end(10)
        self.assertEqual(self.list.get_count(), 2)

    def test_search_item(self):
        self.assertFalse(self.list.search_item(5))
        self.list.insert_at_end(5)
        self.assertTrue(self.list.search_item(5))
        self.assertFalse(self.list.search_item(10))

    def test_make_new_list(self):
        elements = [1, 2, 3, 4, 5]
        self.list.make_new_list(elements)
        self.assertEqual(self.list.get_count(), 5)
        current = self.list.head
        for element in elements:
            self.assertEqual(current.data, element)
            current = current.next

    def test_circular_reference_prevention(self):
        self.list.insert_at_end(1)
        self.list.insert_at_end(2)
        self.list.insert_at_end(3)
        # Get the last node
        last_node = self.list.head
        while last_node.next:
            last_node = last_node.next
        # Create a circular reference
        last_node.next = self.list.head
        # This should not result in an infinite loop
        count = self.list.get_count()
        self.assertEqual(count, 3)

    def test_is_circular(self):
        self.list.insert_at_end(1)
        self.list.insert_at_end(2)
        self.list.insert_at_end(3)
        self.assertFalse(self.list.is_circular())
        # Create a circular reference
        last_node = self.list.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = self.list.head
        self.assertTrue(self.list.is_circular())


if __name__ == "__main__":
    unittest.main()
