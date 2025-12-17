class MapBase:
    """Classe base abstrata para implementações de map."""

    class _Item:
        """Classe leve e interna para armazenar pares chave-valor."""

        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

        def __repr__(self):
            return f"{self._key}:{self._value}"