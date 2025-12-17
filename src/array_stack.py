from src.exceptions import Empty


class ArrayStack:
    """Implementação de uma Pilha LIFO usando uma lista Python como armazenamento subjacente."""

    def __init__(self):
        """Cria uma pilha vazia."""
        self._data = []

    def __len__(self):
        """Retorna o número de elementos na pilha."""
        return len(self._data)

    def is_empty(self):
        """Retorna True se a pilha estiver vazia."""
        return len(self._data) == 0

    def push(self, e):
        """Adiciona o elemento e ao topo da pilha."""
        self._data.append(e)

    def top(self):
        """Retorna (mas não remove) o elemento no topo da pilha.

        Lança a exceção Empty se a pilha estiver vazia.
        """
        if self.is_empty():
            raise Empty("Pilha vazia")
        return self._data[-1]

    def pop(self):
        """Remove e retorna o elemento do topo da pilha (ou seja, LIFO).

        Lança a exceção Empty se a pilha estiver vazia.
        """
        if self.is_empty():
            raise Empty("Pilha vazia")
        return self._data.pop()
