from src.double_linked_node import DoubleLinkedNode


class _DoublyLinkedBase:
    """Uma classe base que fornece uma representação de lista duplamente encadeada."""

    def __init__(self):
        """Cria uma lista vazia."""
        self._header = DoubleLinkedNode(None, None, None)
        self._trailer = DoubleLinkedNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Retorna o número de elementos na lista."""
        return self._size

    def is_empty(self):
        """Retorna True se a lista estiver vazia."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Adiciona o elemento e entre dois nós existentes e retorna o novo nó."""
        newest = DoubleLinkedNode(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Remove um nó não sentinela da lista e retorna o seu elemento."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def reverse(self):
        """
        Inverte a ordem da lista encadeada in-place.
        """
        current = self._header
        while current is not None:
            temp = current._next
            current._next = current._prev
            current._prev = temp
            current = current._prev
        self._header, self._trailer = self._trailer, self._header