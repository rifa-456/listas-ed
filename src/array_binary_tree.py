from src.binary_tree import BinaryTree


class ArrayBinaryTree(BinaryTree):
    """Representação baseada em array de uma estrutura de árvore binária."""

    class Position(BinaryTree.Position):
        """Uma abstração representando a localização de um único elemento."""

        def __init__(self, container, index):
            """Construtor não deve ser invocado pelo usuário."""
            self._container = container
            self._index = index

        def element(self):
            """Retorna o elemento armazenado nesta Posição."""
            return self._container._data[self._index]

        def __eq__(self, other):
            """Retorna True se other é uma Posição representando a mesma localização."""
            return (
                type(other) is type(self)
                and other._index == self._index
                and other._container is self._container
            )

    def _validate(self, p):
        """Retorna o índice associado, se a posição for válida."""
        if not isinstance(p, self.Position):
            raise TypeError("p deve ser um tipo Position adequado")
        if p._container is not self:
            raise ValueError("p não pertence a este contêiner")
        if p._index >= len(self._data) or self._data[p._index] is None:
            raise ValueError("p não é mais válido")
        return p._index

    def _make_position(self, index):
        """Retorna instância de Position para dado índice (ou None se não houver nó)."""
        if index < len(self._data) and self._data[index] is not None:
            return self.Position(self, index)
        return None

    def _expand_list(self, index):
        """Garante que a lista interna tenha tamanho suficiente para o índice."""
        if index >= len(self._data):
            self._data.extend([None] * (index - len(self._data) + 1))

    def __init__(self):
        """Cria uma árvore binária inicialmente vazia."""
        self._data = []
        self._size = 0

    def __len__(self):
        """Retorna o número total de elementos na árvore."""
        return self._size

    def root(self):
        """Retorna a Posição raiz da árvore (ou None se vazia)."""
        return self._make_position(0)

    def parent(self, p):
        """Retorna a Posição do pai de p (ou None se p for raiz)."""
        index = self._validate(p)
        if index == 0:
            return None
        parent_index = (index - 1) // 2
        return self._make_position(parent_index)

    def left(self, p):
        """Retorna a Posição do filho esquerdo de p (ou None)."""
        index = self._validate(p)
        left_index = 2 * index + 1
        return self._make_position(left_index)

    def right(self, p):
        """Retorna a Posição do filho direito de p (ou None)."""
        index = self._validate(p)
        right_index = 2 * index + 2
        return self._make_position(right_index)

    def num_children(self, p):
        """Retorna o número de filhos da Posição p."""
        index = self._validate(p)
        count = 0
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(self._data) and self._data[left_index] is not None:
            count += 1
        if right_index < len(self._data) and self._data[right_index] is not None:
            count += 1
        return count

    def add_root(self, e):
        """Coloca o elemento e na raiz de uma árvore vazia."""
        if self._size > 0:
            raise ValueError("A raiz já existe")
        self._expand_list(0)
        self._data[0] = e
        self._size = 1
        return self._make_position(0)

    def add_left(self, p, e):
        """Cria novo filho esquerdo para p, armazenando e."""
        index = self._validate(p)
        left_index = 2 * index + 1
        if left_index < len(self._data) and self._data[left_index] is not None:
            raise ValueError("O filho à esquerda já existe")

        self._expand_list(left_index)
        self._data[left_index] = e
        self._size += 1
        return self._make_position(left_index)

    def add_right(self, p, e):
        """Cria novo filho direito para p, armazenando e."""
        index = self._validate(p)
        right_index = 2 * index + 2
        if right_index < len(self._data) and self._data[right_index] is not None:
            raise ValueError("O filho à direita já existe")

        self._expand_list(right_index)
        self._data[right_index] = e
        self._size += 1
        return self._make_position(right_index)

    def replace(self, p, e):
        """Substitui o elemento na posição p por e, e retorna o elemento antigo."""
        index = self._validate(p)
        old = self._data[index]
        self._data[index] = e
        return old

    def delete(self, p):
        """Remove o nó em p, substituindo-o pelo seu filho (se houver)."""
        index = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p tem dois filhos")
        child_index = None
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self._data) and self._data[left] is not None:
            child_index = left
        elif right < len(self._data) and self._data[right] is not None:
            child_index = right
        element = self._data[index]
        if child_index is not None:
            self._move_subtree(child_index, index)
        else:
            self._data[index] = None
        self._size -= 1
        return element

    def attach(self, p, t1, t2):
        """Anexa árvores t1 e t2 como subárvores esquerda e direita de p."""
        index = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            self._copy_subtree(t1, 0, 2 * index + 1)
            t1._data = []
            t1._size = 0
        if not t2.is_empty():
            self._copy_subtree(t2, 0, 2 * index + 2)
            t2._data = []
            t2._size = 0

    def _move_subtree(self, src_idx, dest_idx):
        """Move recursivamente o nó de src_idx para dest_idx e seus descendentes."""
        self._expand_list(dest_idx)
        self._data[dest_idx] = self._data[src_idx]
        self._data[src_idx] = None
        src_left = 2 * src_idx + 1
        src_right = 2 * src_idx + 2
        dest_left = 2 * dest_idx + 1
        dest_right = 2 * dest_idx + 2
        if src_left < len(self._data) and self._data[src_left] is not None:
            self._move_subtree(src_left, dest_left)
        if src_right < len(self._data) and self._data[src_right] is not None:
            self._move_subtree(src_right, dest_right)

    def _copy_subtree(self, other_tree, src_idx, dest_idx):
        """Copia recursivamente subárvore de other_tree[src] para self[dest]."""
        element = other_tree._data[src_idx]
        self._expand_list(dest_idx)
        self._data[dest_idx] = element
        src_left = 2 * src_idx + 1
        src_right = 2 * src_idx + 2
        dest_left = 2 * dest_idx + 1
        dest_right = 2 * dest_idx + 2
        if src_left < len(other_tree._data) and other_tree._data[src_left] is not None:
            self._copy_subtree(other_tree, src_left, dest_left)
        if (
            src_right < len(other_tree._data)
            and other_tree._data[src_right] is not None
        ):
            self._copy_subtree(other_tree, src_right, dest_right)
