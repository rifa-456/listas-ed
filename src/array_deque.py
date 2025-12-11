from src.exceptions import Empty


class ArrayDeque:
    """Implementação de fila de duas pontas (deque) usando uma lista Python como armazenamento subjacente."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Cria um deque vazio."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Retorna o número de elementos no deque."""
        return self._size

    def is_empty(self):
        """Retorna True se o deque estiver vazio."""
        return self._size == 0

    def first(self):
        """Retorna (mas não remove) o elemento na frente do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    def last(self):
        """Retorna (mas não remove) o elemento no final do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        """Adiciona um elemento à frente do deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Adiciona um elemento ao final do deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove e retorna o primeiro elemento do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        """Remove e retorna o último elemento do deque.

        Lança a exceção Empty se o deque estiver vazio.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer

    def _resize(self, cap):
        """Redimensiona para uma nova lista com capacidade >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0