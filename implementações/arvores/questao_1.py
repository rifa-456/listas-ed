from src.linked_binary_tree import LinkedBinaryTree

if __name__ == "__main__":
    tree = LinkedBinaryTree()
    root_pos = tree.add_root("Nó Raiz")
    left_pos = tree.add_left(root_pos, "Filho Esq")
    right_pos = tree.add_right(root_pos, "Filho Dir")
    left_left_pos = tree.add_left(left_pos, "Neto Esq-Esq")
    print(f"-----------------------------------")
    tree.show("Árvore Inicial")
    print(f"-----------------------------------")
    old_root_value = tree.replace(root_pos, "Nova Raiz")
    print(
        f"\nValor da raiz substituído de '{old_root_value}' para '{tree.root().element()}'\n"
    )
    deleted_element = tree.delete(right_pos)
    print(f"Elemento removido: {deleted_element}\n")
    print(f"-----------------------------------")
    tree.show("Após Remoção e Substituição")
    print(f"-----------------------------------")
    tree1 = LinkedBinaryTree()
    root1 = tree1.add_root("Raiz T1")
    tree2 = LinkedBinaryTree()
    root2 = tree2.add_root("Raiz T2")
    right_pos = tree.add_right(root_pos, "Filho Dir")
    tree.attach(right_pos, tree1, tree2)
    tree.show("Após Anexar (Attach)")
