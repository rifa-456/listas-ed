from src.linked_binary_tree import LinkedBinaryTree


def is_sum_tree(tree: LinkedBinaryTree):
    """
    Verifica se a árvore binária dada satisfaz a propriedade de Árvore Soma.
    """

    def _check_node(p):
        if p is None:
            return True, 0
        if tree.num_children(p) == 0:
            return True, p.element()
        left_p = tree.left(p)
        right_p = tree.right(p)
        is_left_valid, left_total_sum = _check_node(left_p) if left_p else (True, 0)
        is_right_valid, right_total_sum = _check_node(right_p) if right_p else (True, 0)
        node_value = p.element()
        condition_met = node_value == left_total_sum + right_total_sum
        is_current_valid = is_left_valid and is_right_valid and condition_met
        total_weight = node_value + left_total_sum + right_total_sum
        return is_current_valid, total_weight

    if tree.is_empty():
        return True
    valid, _ = _check_node(tree.root())
    return valid


if __name__ == "__main__":
    T = LinkedBinaryTree()
    root = T.add_root(44)
    node_9 = T.add_left(root, 9)
    node_13 = T.add_right(root, 13)
    p_4 = T.add_left(node_9, 4)
    T.add_right(node_9, 5)
    T.add_left(node_13, 6)
    T.add_right(node_13, 7)
    print(f"-----------------------------------")
    T.show("Árvore Soma Original")
    resultado = is_sum_tree(T)
    print(f"Verificação: A árvore é uma 'Árvore Soma'? -> {resultado}")
    print(f"-----------------------------------")
    old_val = T.replace(p_4, 100)
    T.show("Árvore Modificada (Inválida)")
    resultado_falha = is_sum_tree(T)
    print(f"Resultado após modificação: É árvore soma? -> {resultado_falha}")
    print(f"-----------------------------------")
