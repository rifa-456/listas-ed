from src.linked_binary_tree import LinkedBinaryTree


def encontrar_ancestrais(tree, valor_alvo):
    """
    Encontra e imprime os ancestrais de um nó com valor_alvo.
    Retorna uma lista com os ancestrais encontrados (do mais próximo ao mais distante).
    """
    ancestrais = []

    if tree.is_empty():
        return ancestrais

    def _buscar_recursivamente(p):
        """
        Retorna True se o valor_alvo for encontrado na subárvore enraizada em p.
        Caso encontre nos filhos, adiciona p à lista de ancestrais.
        """
        if p is None:
            return False
        if p.element() == valor_alvo:
            return True
        encontrado_esquerda = False
        if tree.left(p) is not None:
            encontrado_esquerda = _buscar_recursivamente(tree.left(p))
        encontrado_direita = False
        if not encontrado_esquerda and tree.right(p) is not None:
            encontrado_direita = _buscar_recursivamente(tree.right(p))
        if encontrado_esquerda or encontrado_direita:
            ancestrais.append(p.element())
            return True
        return False

    found = _buscar_recursivamente(tree.root())
    if not found:
        print(f"O nó {valor_alvo} não existe na árvore.")

    return ancestrais


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
    T.show("Árvore de Ancestrais")
    print(f"-----------------------------------")
    lista_9 = encontrar_ancestrais(T, 9)
    print(f"Ancestrais do nó 9: {lista_9}")
    lista_6 = encontrar_ancestrais(T, 6)
    print(f"Ancestrais do nó 6: {lista_6}")
    lista_5 = encontrar_ancestrais(T, 5)
    print(f"Ancestrais do nó 5: {lista_5}")
    print(f"--- Teste Nó Inexistente (100) ---")
    lista_100 = encontrar_ancestrais(T, 100)
    print(f"-----------------------------------")
