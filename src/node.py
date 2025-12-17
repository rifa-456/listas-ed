class Node:
    """Classe para armazenar um nó simplesmente encadeado."""

    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next
