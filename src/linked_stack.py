from src.exceptions import Empty
from src.node import Node


class LinkedStack:
    """Implementação de Pilha LIFO usando uma lista simplesmente encadeada para armazenamento."""

    def __init__(self):
        """Cria uma pilha vazia."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Retorna o número de elementos na pilha."""
        return self._size

    def is_empty(self):
        """Retorna True se a pilha estiver vazia."""
        return self._size == 0

    def push(self, e):
        """Adiciona o elemento e ao topo da pilha."""
        self._head = Node(e, self._head)
        self._size += 1

    def top(self):
        """Retorna (mas não remove) o elemento no topo da pilha.

        Lança a exceção Empty se a pilha estiver vazia.
        """
        if self.is_empty():
            raise Empty("Pilha vazia")
        return self._head._element

    def pop(self):
        """Remove e retorna o elemento do topo da pilha (ou seja, LIFO).

        Lança a exceção Empty se a pilha estiver vazia.
        """
        if self.is_empty():
            raise Empty("Pilha vazia")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
