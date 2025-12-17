from src.linked_binary_tree import LinkedBinaryTree


def imprimir_caminhos_raiz_ate_folha(tree: LinkedBinaryTree):
    """
    Imprime todos os caminhos do nó raiz até cada nó folha em uma árvore binária.
    """
    if tree.is_empty():
        print("A árvore está vazia.")
        return
    caminho_atual = []

    def _dfs(p):
        """Função interna de busca em profundidade (DFS)."""
        caminho_atual.append(str(p.element()))
        eh_folha = tree.left(p) is None and tree.right(p) is None
        if eh_folha:
            print(" -> ".join(caminho_atual))
        else:
            if tree.left(p) is not None:
                _dfs(tree.left(p))
            if tree.right(p) is not None:
                _dfs(tree.right(p))
        caminho_atual.pop()

    print("--- Caminhos da Raiz até as Folhas ---")
    _dfs(tree.root())


if __name__ == "__main__":
    T = LinkedBinaryTree()
    root = T.add_root(1)
    p2 = T.add_left(root, 2)
    p3 = T.add_right(root, 3)
    T.add_left(p2, 4)
    T.add_right(p2, 5)
    p6 = T.add_left(p3, 6)
    p7 = T.add_right(p3, 7)
    T.add_left(p6, 8)
    T.add_right(p7, 9)
    print(f"-----------------------------------")
    T.show("Árvore de Caminhos")
    print(f"-----------------------------------")
    imprimir_caminhos_raiz_ate_folha(T)
    print(f"-----------------------------------")
