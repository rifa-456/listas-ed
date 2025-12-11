from src.exceptions import Empty


class ArrayQueue:
    """Implementação de fila FIFO usando uma lista Python como armazenamento subjacente."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Cria uma fila vazia."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

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
        return self._data[self._front]

    def dequeue(self):
        """Remove e retorna o primeiro elemento da fila (ou seja, FIFO).

        Lança a exceção Empty se a fila estiver vazia.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Adiciona um elemento ao final da fila."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Redimensiona para uma nova lista com capacidade ≥ len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0