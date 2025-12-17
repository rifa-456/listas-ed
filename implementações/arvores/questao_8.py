from src.linked_binary_tree import LinkedBinaryTree


def substituir_pela_soma_subarvores(tree):
    """
    Substitui o valor de cada nó pela soma de todos os elementos
    presentes em suas subárvores esquerda e direita.
    """

    def _processar_no(p):
        """
        Retorna a soma da subárvore enraizada em p (valor original + filhos).
        """
        if p is None:
            return 0
        soma_total_esq = _processar_no(tree.left(p)) if tree.left(p) else 0
        soma_total_dir = _processar_no(tree.right(p)) if tree.right(p) else 0
        valor_original = p.element()
        novo_valor = soma_total_esq + soma_total_dir
        tree.replace(p, novo_valor)
        return valor_original + novo_valor

    if not tree.is_empty():
        _processar_no(tree.root())


if __name__ == "__main__":
    T = LinkedBinaryTree()
    root = T.add_root(1)
    p2 = T.add_left(root, 2)
    p3 = T.add_right(root, 3)
    T.add_left(p2, 4)
    p5 = T.add_left(p3, 5)
    p6 = T.add_right(p3, 6)
    T.add_left(p5, 7)
    T.add_right(p5, 8)
    print(f"-----------------------------------")
    try:
        T.show("Árvore Original")
    except AttributeError:
        print("Método 'show' não encontrado na classe base.")
        print(f"Preorder: {[p.element() for p in T.preorder()]}")
    print(f"-----------------------------------")
    print("Executando: Substituir pela Soma das Subárvores...")
    substituir_pela_soma_subarvores(T)
    print(f"-----------------------------------")
    T.show("Árvore Transformada")
    print(f"-----------------------------------")
