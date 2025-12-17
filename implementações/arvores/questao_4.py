from src.linked_binary_tree import LinkedBinaryTree


def are_identical(tree1: LinkedBinaryTree, tree2: LinkedBinaryTree) -> bool:
    """
    Verifica se duas árvores são idênticas (mesma estrutura e mesmos valores).
    """

    def check_subtree(p1, p2) -> bool:
        if p1 is None and p2 is None:
            return True
        if p1 is None or p2 is None:
            return False
        if p1.element() != p2.element():
            return False
        return check_subtree(tree1.left(p1), tree2.left(p2)) and check_subtree(
            tree1.right(p1), tree2.right(p2)
        )

    return check_subtree(tree1.root(), tree2.root())


if __name__ == "__main__":
    t1 = LinkedBinaryTree()
    root1 = t1.add_root(1)
    l1 = t1.add_left(root1, 2)
    r1 = t1.add_right(root1, 3)
    t1.add_left(l1, 4)
    t1.add_right(l1, 5)
    t2 = LinkedBinaryTree()
    root2 = t2.add_root(1)
    l2 = t2.add_left(root2, 2)
    r2 = t2.add_right(root2, 3)
    t2.add_left(l2, 4)
    t2.add_right(l2, 5)
    print(f"-----------------------------------")
    t1.show("Árvore 1")
    print(f"-----------------------------------")
    t2.show("Árvore 2")
    print(f"-----------------------------------")
    result = are_identical(t1, t2)
    status = "IDÊNTICAS" if result else "DIFERENTES"
    print(f"Resultado da comparação: As árvores são {status}.")
