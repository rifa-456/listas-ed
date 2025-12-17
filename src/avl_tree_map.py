from src.tree_map import TreeMap


class AVLTreeMap(TreeMap):
    """Implementação de mapa ordenado usando uma árvore AVL."""

    class _Node(TreeMap._Node):
        """Classe Node para AVL mantém valor de altura para balanceamento."""

        __slots__ = "_height"

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

    def _recompute_height(self, p):
        """Recalcula a altura da posição p com base nas alturas de seus filhos."""
        node = self._validate(p)
        node._height = 1 + max(self._height(self.left(p)), self._height(self.right(p)))

    def _isbalanced(self, p):
        """Retorna True se a posição p tem fator de balanceamento entre -1 e 1."""
        return abs(self._height(self.left(p)) - self._height(self.right(p))) <= 1

    def _height(self, p):
        """Retorna a altura da subárvore enraizada na Posição p."""
        if p is None:
            return 0
        else:
            return p._node._height

    def _tall_child(self, p, favorleft=False):
        """Retorna o filho mais alto de p (favorece o filho esquerdo se as alturas forem iguais)."""
        if self._height(self.left(p)) + (1 if favorleft else 0) > self._height(
            self.right(p)
        ):
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        """Retorna o neto mais alto de p, favorecendo alinhamento para desempate."""
        child = self._tall_child(p)
        alignment = child == self.left(p)
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        """Rebalanceia a árvore começando na posição p e subindo."""
        while p is not None:
            old_height = self._height(p)
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if self._height(p) == old_height:
                p = None
            else:
                p = self.parent(p)

    def _rebalance_insert(self, p):
        """Rebalanceia a árvore após uma inserção na posição p."""
        self._rebalance(p)

    def _rebalance_delete(self, p):
        """Rebalanceia a árvore após uma deleção na posição p."""
        self._rebalance(p)
