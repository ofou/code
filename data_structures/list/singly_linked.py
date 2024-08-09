class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return f"Node({self.data})"

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SinglyLinkedList({list(self)})"

    def __iter__(self):
        visited = set()
        current = self.head
        while current and current not in visited:
            visited.add(current)
            yield current.data
            current = current.next

    def __len__(self):
        return sum(1 for _ in self)

    def __bool__(self):
        return self.head is not None

    def print_list(self):
        print(*self, sep=" ")

    def insert_at_beginning(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        visited = set()
        current = self.head
        while current.next and current.next not in visited:
            visited.add(current)
            current = current.next
        current.next = new_node

    def insert_after_item(self, x, data):
        current = self.head
        visited = set()
        while current and current not in visited:
            if current.data == x:
                new_node = self.Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            visited.add(current)
            current = current.next
        print("Item not in the list")

    def insert_before_item(self, x, data):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == x:
            self.insert_at_beginning(data)
            return
        prev = None
        current = self.head
        visited = set()
        while current and current not in visited:
            if current.data == x:
                new_node = self.Node(data)
                new_node.next = current
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node
                return
            visited.add(current)
            prev = current
            current = current.next
        print("Item not in the list")

    def get_count(self):
        return len(self)

    def search_item(self, x):
        return any(data == x for data in self)

    def make_new_list(self, elements):
        self.head = None
        for element in elements:
            self.insert_at_end(element)

    def is_circular(self):
        if not self.head:
            return False
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
