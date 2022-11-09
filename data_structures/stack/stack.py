class Stack:
    """
    Simple stack implementation using a list
    """

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        """check if the stack is empty"""
        return self.items == []

    def push(self, item: any) -> None:
        """push an item to the top of the stack"""
        self.items.append(item)

    def pop(self) -> any:
        """pop the top item of the stack"""
        return self.items.pop()

    def peek(self) -> any:
        """peek at the top item of the stack"""
        return self.items[len(self.items)-1]

    def size(self) -> int:
        """return the size of the stack"""
        return len(self.items)
