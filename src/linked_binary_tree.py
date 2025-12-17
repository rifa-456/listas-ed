from src.binary_tree import BinaryTree
from src.linked_deque import LinkedDeque


class LinkedBinaryTree(BinaryTree):
    """Representação encadeada de uma estrutura de árvore binária."""

    class _Node:
        """Classe leve e interna para armazenar um nó."""

        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """Uma abstração representando a localização de um único elemento."""

        def __init__(self, container, node):
            """O construtor não deve ser invocado pelo usuário."""
            self._container = container
            self._node = node

        def element(self):
            """Retorna o elemento armazenado nesta Posição."""
            return self._node._element

        def __eq__(self, other):
            """Retorna True se other for uma Posição representando a mesma localização."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Retorna o nó associado, se a posição for válida."""
        if not isinstance(p, self.Position):
            raise TypeError("p deve ser um tipo Position adequado")
        if p._container is not self:
            raise ValueError("p não pertence a este contêiner")
        if p._node._parent is p._node:
            raise ValueError("p não é mais válido")
        return p._node

    def _make_position(self, node):
        """Retorna a instância de Position para o nó dado (ou None se não houver nó)."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Cria uma árvore binária inicialmente vazia."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Retorna o número total de elementos na árvore."""
        return self._size

    def root(self):
        """Retorna a Posição raiz da árvore (ou None se a árvore estiver vazia)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Retorna a Posição do pai de p (ou None se p for a raiz)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Retorna a Posição do filho à esquerda de p (ou None se não houver)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Retorna a Posição do filho à direita de p (ou None se não houver)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Retorna o número de filhos da Posição p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        """Coloca o elemento e na raiz de uma árvore vazia e retorna a nova Posição.

        Lança ValueError se a árvore não estiver vazia.
        """
        if self._root is not None:
            raise ValueError("A raiz já existe")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """Cria um novo filho à esquerda para a Posição p, armazenando o elemento e.

        Retorna a Posição do novo nó.
        Lança ValueError se a Posição p for inválida ou se p já tiver um filho à esquerda.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("O filho à esquerda já existe")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def add_right(self, p, e):
        """Cria um novo filho à direita para a Posição p, armazenando o elemento e.

        Retorna a Posição do novo nó.
        Lança ValueError se a Posição p for inválida ou se p já tiver um filho à direita.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("O filho à direita já existe")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def replace(self, p, e):
        """Substitui o elemento na posição p por e, e retorna o elemento antigo."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """Remove o nó na Posição p, substituindo-o pelo seu filho, se houver.

        Retorna o elemento que estava armazenado na Posição p.
        Lança ValueError se a Posição p for inválida ou se p tiver dois filhos.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p tem dois filhos")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def attach(self, p, t1, t2):
        """Anexa as árvores t1 e t2 como subárvores esquerda e direita da folha externa p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("a posição deve ser uma folha")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Os tipos das árvores devem coincidir")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def breadth_first(self):
        """Gera uma iteração em largura (Breadth-First) das posições da árvore."""
        if not self.is_empty():
            fringe = LinkedDeque()
            fringe.insert_last(self.root())
            while not fringe.is_empty():
                p = fringe.delete_first()
                yield p
                for c in self.children(p):
                    fringe.insert_last(c)
