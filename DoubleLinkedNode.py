#!/usr/bin/env python3

class DoubleLinkedNode:

    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


if __name__ == "__main__":

    print(f"===============================")

    n1 = DoubleLinkedNode(5)
    n2 = DoubleLinkedNode(7)
    n3 = DoubleLinkedNode(10)

    n1.next = n2
    n2.prev = n1

    n2.next = n3
    n3.prev = n2

    print(f"====Node 1====\n"
      f"Location: {n1}\n"
      f"Value: {n1.value}\n"
      f"prev node: None\n"
      f"next node: {n1.next.value}\n")

    print(f"====Node 2====\n"
      f"Location: {n2}\n"
      f"Value: {n2.value}\n"
      f"prev node: {n2.prev.value}\n"
      f"next node: {n2.next.value}\n")

    print("f====Node 3====\n"
      f"Location: {n3}\n"
      f"Value: {n3.value}\n"
      f"prev node: {n3.prev.value}\n"
      f"next node: None")
