from __future__ import annotations
from typing import Any

class Node:
    """Esta classe representa um nó de uma lista encadeada."""
    def __init__(self, data: int = 0, next_node: Node | None=None) -> None:
        self.data = data
        self.next = next_node

    def __repr__(self) -> str:
        return f"{self.data} -> {repr(self.next)}"

class LinkedList:
    """Esta classe representa uma lista encadeada."""
    def __init__(self, head: Node | None = None) -> None:
        self.head = head

    def __repr__(self) -> str:
        return f'[{self.head}]'
    
    def insert(self, data: int, position: int = 0):
        new_node = Node(data)

        if self.head is None:
            if position == 0:
                self.head = new_node
                return
            else:
                raise IndexError()

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        current_position = 0

        while current_position < position - 1:
            if current_node.next is None:
                raise IndexError()
            current_node = current_node.next
            current_position += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, position: int):
        if self.head is None:
            raise IndexError("Linked list is already empty")
        
        if position == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_position = 0

        while current_position < position - 1:
            if current_node.next is None:
                raise IndexError()
            current_node = current_node.next
            current_position += 1

        if current_node.next is None:
            raise IndexError()
        else:
            current_node.next = current_node.next.next
        

    def has_element(self, element: int):
        current = self.head
        has_found = False

        while current != None and not has_found:
            if current.data == element:
                has_found = True
            else:
                current = current.next

        return has_found        

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

