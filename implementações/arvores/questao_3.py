from src.linked_binary_tree import LinkedBinaryTree

if __name__ == "__main__":
    tree = LinkedBinaryTree()
    root = tree.add_root("+")
    mult1 = tree.add_left(root, "*")
    tree.add_left(mult1, "2")
    minus = tree.add_right(mult1, "-")
    tree.add_left(minus, "a")
    tree.add_right(minus, "1")
    mult2 = tree.add_right(root, "*")
    tree.add_left(mult2, "3")
    tree.add_right(mult2, "b")
    print(f"-----------------------------------")
    try:
        tree.show("Árvore de Expressão")
    except AttributeError:
        print("Método 'show' não encontrado na classe base.")
    print(f"-----------------------------------")
    print(f"1. Preorder (Pré-ordem): {[str(p.element()) for p in tree.preorder()]}")
    print(f"2. Postorder (Pós-ordem): {[str(p.element()) for p in tree.postorder()]}")
    print(f"3. Inorder (Ordem Simétrica): {[str(p.element()) for p in tree.inorder()]}")
