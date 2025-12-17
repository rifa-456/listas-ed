class Tree:
    """Classe base abstrata representando uma estrutura de árvore."""

    class Position:
        """Uma abstração representando a localização de um único elemento."""

        def element(self):
            """Retorna o elemento armazenado nesta Posição."""
            raise NotImplementedError()

        def __eq__(self, other):
            """Retorna True se other for uma Posição representando a mesma localização."""
            raise NotImplementedError()

        def __ne__(self, other):
            """Retorna True se other não representar a mesma localização."""
            return not (self == other)

    def root(self):
        """Retorna a Posição da raiz da árvore (ou None se vazia)."""
        raise NotImplementedError()

    def parent(self, p):
        """Retorna a Posição do pai de p (ou None se p for a raiz)."""
        raise NotImplementedError()

    def num_children(self, p):
        """Retorna o número de filhos da Posição p."""
        raise NotImplementedError()

    def children(self, p):
        """Gera uma iteração das Posições representando os filhos de p."""
        raise NotImplementedError()

    def __len__(self):
        """Retorna o número total de elementos na árvore."""
        raise NotImplementedError()

    def is_root(self, p):
        """Retorna True se a Posição p representar a raiz da árvore."""
        return self.root() == p

    def is_leaf(self, p):
        """Retorna True se a Posição p não tiver filhos."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Retorna True se a árvore estiver vazia."""
        return len(self) == 0
