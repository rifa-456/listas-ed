from src.exceptions import Empty
from src.node import Node


class CircularQueue:
    """Implementação de fila usando lista encadeada circular para armazenamento."""

    def __init__(self):
        """Cria uma fila vazia."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Retorna o número de elementos na fila."""
        return self._size

    def is_empty(self):
        """Retorna True se a fila estiver vazia."""
        return self._size == 0

    def first(self):
        """Retorna (mas não remove) o elemento na frente da fila.

        Lança a exceção Empty se a fila estiver vazia.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove e retorna o primeiro elemento da fila (ou seja, FIFO).

        Lança a exceção Empty se a fila estiver vazia.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Adiciona um elemento ao final da fila."""
        newest = Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotaciona o elemento da frente para o final da fila."""
        if self._size > 0:
            self._tail = self._tail._next