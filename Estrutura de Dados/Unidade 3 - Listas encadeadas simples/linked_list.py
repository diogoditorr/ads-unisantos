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
        current_node = self.head
        current_position = 0

        if current_node is not None:
            while current_node.next != None:
                if current_position == (position - 1):
                    node = Node(data)
                    node.next = current_node.next
                    current_node.next = node
                else:
                    current_node = current_node.next

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

def main():
    lista_encadeada = LinkedList()
    print("Lista vazia:\n", lista_encadeada.is_empty())

    lista_encadeada.insert(5)
    print("Lista contém um único elemento:\n", lista_encadeada)

    lista_encadeada.insert(10)
    print("Inserindo um novo elemento\n", lista_encadeada)
    print("Existe um elemento com valor 10?", lista_encadeada.has_element(10))
    print("Existe um elemento com valor 9?", lista_encadeada.has_element(9))

if __name__ == '__main__':
    main()
