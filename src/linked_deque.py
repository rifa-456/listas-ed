from src._doubly_linked_base import _DoublyLinkedBase
from src.exceptions import Empty


class LinkedDeque(_DoublyLinkedBase):
    """Implementação de fila de duas pontas (deque) usando uma lista duplamente encadeada."""

    def first(self):
        """Retorna (mas não remove) o elemento na frente do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """Retorna (mas não remove) o elemento no final do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Adiciona um elemento à frente do deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Adiciona um elemento ao final do deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove e retorna o primeiro elemento do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove e retorna o último elemento do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)