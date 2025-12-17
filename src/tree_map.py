from src.linked_binary_tree import LinkedBinaryTree
from src.map_base import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Implementação de map ordenado usando uma árvore binária de busca."""

    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Retorna a chave do par chave-valor do map."""
            return self.element()._key

        def value(self):
            """Retorna o valor do par chave-valor do map."""
            return self.element()._value

    def _subtree_search(self, p, k):
        """Retorna a Posição da subárvore de p tendo chave k, ou último nó procurado."""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """Retorna a Posição do primeiro item na subárvore enraizada em p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Retorna a Posição do último item na subárvore enraizada em p."""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """Retorna a primeira Posição na árvore (ou None se vazia)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Retorna a última Posição na árvore (ou None se vazia)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Retorna a Posição logo antes de p na ordem natural."""
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Retorna a Posição logo após p na ordem natural."""
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Retorna posição com chave k, ou vizinho (ou None se vazia)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        """Retorna par (chave, valor) com chave mínima (ou None se vazia)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Retorna par (chave, valor) com menor chave maior ou igual a k."""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Itera todos os pares (chave, valor) tal que start <= chave < stop."""
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    # -------------------- Map operations --------------------
    def __getitem__(self, k):
        """Retorna valor associado com chave k (levanta KeyError se não encontrada)."""
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError("Key Error: " + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Atribui valor v à chave k, sobrescrevendo valor existente se presente."""
        if self.is_empty():
            leaf = self.add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self.add_right(p, item)
                else:
                    leaf = self.add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        """Gera uma iteração de todas as chaves do map em ordem."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove o item na Posição dada."""
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self.replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        super().delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        """Remove item associado com chave k (levanta KeyError se não encontrada)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError("Key Error: " + repr(k))

    def _rebalance_insert(self, p):
        """Hook para subclasses balanceadas chamado após inserção."""
        pass

    def _rebalance_delete(self, p):
        """Hook para subclasses balanceadas chamado após deleção."""
        pass

    def _rebalance_access(self, p):
        """Hook para subclasses balanceadas chamado após acesso."""
        pass


    def _restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x

    def _rotate(self, p):
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent