class DoubleLinkedNode:
    """Classe para armazenar um nó duplamente encadeado."""
    __slots__ = '_element', '_prev', '_next'

    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next