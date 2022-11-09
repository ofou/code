
import pytest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.print_list()
        >>> sll.insert_at_end(1)
        >>> sll.insert_at_end(2)
        >>> sll.insert_at_end(3)
        >>> sll.print_list()
        1 2 3
        >>> sll.insert_at_beginning(0)
        >>> sll.print_list()
        0 1 2 3
        """
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

    def insert_at_beginning(self, data):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.insert_at_beginning(1)
        >>> sll.print_list()
        1
        >>> sll.insert_at_beginning(2)
        >>> sll.print_list()
        2 1
        >>> sll.insert_at_beginning(3)
        >>> sll.print_list()
        3 2 1
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.insert_at_end(1)
        >>> sll.print_list()
        1
        >>> sll.insert_at_end(2)
        >>> sll.print_list()
        1 2
        >>> sll.insert_at_end(3)
        >>> sll.print_list()
        1 2 3
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def insert_after_item(self, x, data):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.insert_after_item(1, 2)
        Item not in the list
        >>> sll.insert_at_end(1)
        >>> sll.insert_after_item(1, 2)
        >>> sll.print_list()
        1 2
        >>> s
        """
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_before_item(self, x, data):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.insert_before_item(1, 2)
        Item not in the list
        >>> sll.insert_at_end(1)
        >>> sll.insert_before_item(1, 2)
        >>> sll.print_list()
        2 1
        >>> sll.insert_before_item(1, 3)
        >>> sll.print_list()
        2 3 1
        """
        if self.head is None:
            print("List is empty")
            return
        if x == self.head.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def get_count(self):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.get_count()
        0
        >>> sll.insert_at_end(1)
        >>> sll.insert_at_end(2)
        >>> sll.insert_at_end(3)
        >>> sll.get_count()
        3
        """
        if self.head is None:
            return 0
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.next
        return count

    def search_item(self, x):
        """
        >>> sll = SinglyLinkedList()
        >>> sll.search_item(1)
        False
        >>> sll.insert_at_end(1)
        >>> sll.insert_at_end(2)
        >>> sll.insert_at_end(3)
        >>> sll.search_item(1)
        True
        >>> sll.search_item(4)
        False
        """
        if self.head is None:
            return False
        n = self.head
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False

    def make_new_node(self, data):
        new_node = Node(data)
        return new_node


# Test using pytest

def test_singly_linked_list():
    sll = SinglyLinkedList()
    sll.insert_at_beginning(1)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(3)
    assert sll.get_count() == 3
    assert sll.search_item(1) is True
    assert sll.search_item(4) is False
    sll.insert_after_item(1, 2)
    assert sll.get_count() == 4
    sll.insert_before_item(1, 3)
    assert sll.get_count() == 5
    sll.insert_at_end(4)
    assert sll.get_count() == 6
    sll.print_list()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_singly_linked_list()
