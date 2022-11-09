#!/usr/bin/env python3

from DoubleLinkedNode import DoubleLinkedNode as Node


class DoubleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self._length = 0

    def __len__(self):
        return self._length

    def _get_node(self, index):
        if index >= self._length or index < 0:
            raise IndexError("List index out of range")

        current_node = self.start
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node

    def print_forward(self):
        node = self.start
        node_index = 0
        while node != None:
            print(f"==== {node_index} ====")
            print(node.value)
            node = node.next
            node_index += 1
            print("***********")

    def print_backward(self):
        node = self.end
        node_index = self._length - 1
        while node != None:
            print(f"==== {node_index} ====")
            print(node.value)
            node = node.prev
            node_index -= 1
            print("***********")

    def get_value(self, index):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")

        current_node = self._get_node(index)
        node_val = current_node.value
        return node_val

    def insert(self, index, val):
        if index > self._length or index < 0:
            raise IndexError("List index out of range")

        new_node = Node(val)

        if self._length == 0:
            self.start = new_node
            self.end = new_node
            self._length += 1
            return

        if index == 0:
            first = self.start
            self.start = new_node
            new_node.next = first
            first.prev = new_node
            self._length += 1
            return

        if index == self._length:
            last = self.end
            self.end = new_node
            new_node.prev = last
            last.next = self.end
            self._length += 1
            return

        after_node = self._get_node(index)
        before_node = after_node.prev

        before_node.next = new_node
        new_node.prev = before_node

        new_node.next = after_node
        after_node.prev = new_node

        self._length += 1

        print(f"new node index: {index}")
        print(f"new node value: {new_node.value}")

    def append(self, val):
        end_index = self._length
        self.insert(end_index, val)

    def prepend(self, val):
        start_index = 0
        self.insert(start_index, val)

    def pop(self, index):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")

        remove_node = self._get_node(index)
        before_node = remove_node.prev
        after_node = remove_node.next

        before_node.next = after_node
        after_node.prev = before_node

        self._length -= 1

    def remove(self, val):
        if self.length == 0:
            return

        current_node = self.start
        current_index = 0

        while current_node.value != val and current_index < self._length:
            current_node = current_node.next
            current_index += 1

        if current_index == self._length:
            return

        return self.pop(current_index)


if __name__ == "__main__":
    print(f"==== {__file__} ====")

    dll = DoubleLinkedList()

    a = Node("apples")
    b = Node("bananas")
    c = Node("cranberries")

    a.next = b
    b.prev = a

    b.next = c
    c.prev = b

    dll.start = a
    dll.end = c
    dll._length = 3

    print(f"\nValue at node C: {dll.start.next.next.value}")
    print(f"Value at node A: {dll.end.prev.prev.value}")

    print("\n=== Printing forward ======")
    print(dll.print_forward())
    print("\n=== Printing backwards ======")
    print(dll.print_backward())

    print("\n=== Testing ._get_node ======")
    print(dll._get_node(1))

    print("\n=== Testing .get_value ======")
    print(f"[ {dll.get_value(0)} ] *Should print apples")
    print(f"[ {dll.get_value(1)} ] *Should print bananas")
    print(f"[ {dll.get_value(2)} ] *Should print cranberries")

    print("\n=== Testing .insert =====")
    print(dll.insert(1, "apricots"))
    print(dll.print_forward())
    print(f"DoubleLinkedList Length: {dll._length}")

    print("\n=== Testing .append =====")
    print("Item to be appended: dragonfruit")
    print(dll.append("dragonfruit"))
    print(dll.print_forward())

    print("\n=== Testing .prepend =====")
    print("Item to be prepended: acai")
    print(dll.prepend("acai"))
    print(dll.print_backward())

    print("\n=== Testing .pop =====")
    print("Item to be popped: apricots")
    print(dll.pop(2))
    print(dll.print_backward())

    print("\n=== Testing .remove =====")
    print("Removing item not in list: watermelons")
    print(dll.remove("watermelons"))
    print("Removing item that is in the list: acai")
    print(dll.remove("acai"))
