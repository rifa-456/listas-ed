"""
Refactoring:
1. Introduced _get_node_label(p) to allow subclasses to customize node display.
2. Updated _build_tree_string to use this new method.
"""
from src.tree import Tree
from rich.console import Console


class BinaryTree(Tree):
    """Classe base abstrata representando uma estrutura de árvore binária."""

    def left(self, p):
        """Retorna a Posição do filho à esquerda de p (ou None se não houver)."""
        raise NotImplementedError()

    def right(self, p):
        """Retorna a Posição do filho à direita de p (ou None se não houver)."""
        raise NotImplementedError()

    def sibling(self, p):
        """Retorna a Posição representando o irmão de p (ou None se não houver)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Gera uma iteração das Posições representando os filhos de p."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def positions(self):
        """Gera uma iteração de todas as posições da árvore."""
        return self.inorder()

    def __iter__(self):
        """Gera uma iteração dos elementos da árvore."""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Gera uma iteração das posições da árvore em pré-ordem (Preorder)."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Gera uma iteração pré-ordem das posições na subárvore enraizada em p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """Gera uma iteração das posições da árvore em pós-ordem (Postorder)."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Gera uma iteração pós-ordem das posições na subárvore enraizada em p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def inorder(self):
        """Gera uma iteração das posições da árvore em ordem simétrica (Inorder)."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Gera uma iteração em ordem simétrica das posições na subárvore enraizada em p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def show(self, title="Árvore Binária"):
        """Imprime a árvore no console com formatação ASCII visual."""
        console = Console()
        console.print(f"\n[bold underline]{title}[/bold underline]\n")

        if self.is_empty():
            console.print("[dim italic]Árvore Vazia[/dim italic]")
            return

        lines, _, _, _ = self._build_tree_string(self.root())
        for line in lines:
            console.print(f"[bold white]{line}[/bold white]")
        console.print("")

    def _get_node_label(self, p):
        """
        Hook method to customize how a node is displayed in the tree.
        """
        return str(p.element())

    def _build_tree_string(self, p):
        """
        Gera a representação em string da subárvore enraizada em p usando box-drawing chars.
        Retorna: (lines, width, height, midpoint_index)
        """
        label = self._get_node_label(p)
        label_w = len(label)
        left_p = self.left(p)
        right_p = self.right(p)
        if left_p is None and right_p is None:
            return [label], label_w, 1, label_w // 2
        left_lines, left_w, left_h, left_mid = ([], 0, 0, 0)
        right_lines, right_w, right_h, right_mid = ([], 0, 0, 0)
        if left_p:
            left_lines, left_w, left_h, left_mid = self._build_tree_string(left_p)
        if right_p:
            right_lines, right_w, right_h, right_mid = self._build_tree_string(right_p)
        max_h = max(left_h, right_h)
        CHAR_H = "─"
        CHAR_UL = "┌"
        CHAR_UR = "┐"
        CHAR_DL = "└"
        CHAR_DR = "┘"
        CHAR_TEE_UP = "┴"
        spacing = 2
        if left_p and right_p:
            right_offset = left_w + spacing
            conn_left = left_mid
            conn_right = right_offset + right_mid
            root_mid = (conn_left + conn_right) // 2
            root_start = root_mid - (label_w // 2)
            global_shift = 0
            if root_start < 0:
                global_shift = -root_start
                root_start = 0
                conn_left += global_shift
                conn_right += global_shift
                right_offset += global_shift
                root_mid += global_shift
            line_conn_chars = [" "] * (max(right_offset + right_w, conn_right + 1))
            line_conn_chars[conn_left] = CHAR_UL
            line_conn_chars[conn_right] = CHAR_UR
            line_conn_chars[root_mid] = CHAR_TEE_UP
            for i in range(conn_left + 1, root_mid):
                line_conn_chars[i] = CHAR_H
            for i in range(root_mid + 1, conn_right):
                line_conn_chars[i] = CHAR_H
            line_conn = "".join(line_conn_chars)
            line_label = " " * root_start + label
            lines = [line_label, line_conn]
            for i in range(max_h):
                l_str = left_lines[i] if i < left_h else " " * left_w
                r_str = right_lines[i] if i < right_h else " " * right_w
                merged = (" " * global_shift) + l_str + (" " * spacing) + r_str
                lines.append(merged)
            width = max(len(line) for line in lines)
            lines = [line + " " * (width - len(line)) for line in lines]
            return lines, width, len(lines), root_mid

        elif left_p:
            conn_left = left_mid
            root_mid = conn_left + 2
            root_start = root_mid - (label_w // 2)
            global_shift = 0
            if root_start < 0:
                global_shift = -root_start
                root_start = 0
                conn_left += global_shift
                root_mid += global_shift
            line_conn_chars = [" "] * (max(left_w + global_shift, root_mid + 1))
            line_conn_chars[conn_left] = CHAR_UL
            line_conn_chars[root_mid] = CHAR_DR
            for i in range(conn_left + 1, root_mid):
                line_conn_chars[i] = CHAR_H
            line_conn = "".join(line_conn_chars)
            line_label = " " * root_start + label
            lines = [line_label, line_conn]
            for i in range(max_h):
                l_str = left_lines[i] if i < left_h else " " * left_w
                merged = (" " * global_shift) + l_str
                lines.append(merged)
            width = max(len(line) for line in lines)
            lines = [line + " " * (width - len(line)) for line in lines]
            return lines, width, len(lines), root_mid

        elif right_p:
            conn_right = right_mid
            shift_right_block = 2
            root_mid = 0
            conn_right_abs = shift_right_block + conn_right
            min_root_space = (label_w // 2) + 1
            if shift_right_block < min_root_space:
                diff = min_root_space - shift_right_block
                shift_right_block += diff
                conn_right_abs += diff
                root_mid = label_w // 2
            root_start = 0
            width_needed = max(shift_right_block + right_w, conn_right_abs + 1)
            line_conn_chars = [" "] * width_needed
            line_conn_chars[root_mid] = CHAR_DL
            line_conn_chars[conn_right_abs] = CHAR_UR
            for i in range(root_mid + 1, conn_right_abs):
                line_conn_chars[i] = CHAR_H
            line_conn = "".join(line_conn_chars)
            line_label = " " * root_start + label
            lines = [line_label, line_conn]
            for i in range(max_h):
                r_str = right_lines[i] if i < right_h else " " * right_w
                merged = (" " * shift_right_block) + r_str
                lines.append(merged)
            width = max(len(line) for line in lines)
            lines = [line + " " * (width - len(line)) for line in lines]
            return lines, width, len(lines), root_mid
        return [], 0, 0, 0