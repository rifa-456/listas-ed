from src.tree_map import TreeMap


class RedBlackTreeMap(TreeMap):
    """Implementação de map ordenado usando uma árvore rubro-negra."""

    class _Node(TreeMap._Node):
        """Node class que mantém bit que denota cor."""

        __slots__ = "_red"

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True

    def _get_node_label(self, p):
        """
        Override para mostrar cor no label do nó na visualização da árvore.
        Formato: 'chave:valor (RED)' ou 'chave:valor (BLK)'
        """
        base_label = str(p.element())
        color_tag = "RED" if self._is_red(p) else "BLK"
        return f"{base_label} ({color_tag})"

    def _set_red(self, p):
        """Define a posição p como vermelha."""
        p._node._red = True

    def _set_black(self, p):
        """Define a posição p como preta."""
        p._node._red = False

    def _set_color(self, p, make_red):
        """Define a cor da posição p."""
        p._node._red = make_red

    def _is_red(self, p):
        """Retorna True se p for vermelho, None e nós pretos retornam False."""
        return p is not None and p._node._red

    def _is_red_leaf(self, p):
        """Retorna True se p for uma folha vermelha."""
        return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        """Retorna um filho vermelho de p (ou None se não houver nenhum)."""
        for child in [self.left(p), self.right(p)]:
            if self._is_red(child):
                return child
        return None

    def _rebalance_insert(self, p):
        """Rebalanceia após inserção - novo nó é sempre vermelho."""
        self._resolve_red(p)

    def _resolve_red(self, p):
        """Resolve problema de vermelho duplo."""
        if self.is_root(p):
            self._set_black(p)
        else:
            parent = self.parent(p)
            if self._is_red(parent):
                uncle = self.sibling(parent)
                if not self._is_red(uncle):
                    middle = self._restructure(p)
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    grand = self.parent(parent)
                    self._set_red(grand)
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)

    def _rebalance_delete(self, p):
        """Rebalanceia após deleção."""
        if len(self) == 1:
            self._set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
            elif n == 2:
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        """Resolve deficit preto em z, onde y é a raiz da subárvore mais pesada de z."""
        if not self._is_red(y):
            x = self._get_red_child(y)
            if (
                x is not None
            ):
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z)
                elif not self.is_root(z):
                    self._fix_deficit(
                        self.parent(z), self.sibling(z)
                    )
        else:
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))

    def _rebalance_access(self, p):
        """Hook para subclasses balanceadas - sem operação para rubro-negra."""
        pass