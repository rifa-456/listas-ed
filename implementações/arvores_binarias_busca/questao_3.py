from src.red_black_tree_map import RedBlackTreeMap


if __name__ == "__main__":
    tree = RedBlackTreeMap()
    print("\n1. RedBlackTreeMap criado (vazio)")
    print("\n2. Inserindo pares (chave, valor):")
    items = [
        (44, "A"),
        (17, "B"),
        (88, "C"),
        (8, "D"),
        (32, "E"),
        (65, "F"),
        (97, "G"),
        (28, "H"),
        (54, "I"),
        (82, "J"),
        (76, "K"),
        (68, "L"),
    ]
    for i, (k, v) in enumerate(items, 1):
        tree[k] = v
        print(f"\n   [{i}] Inserido: {k} -> {v}")
    print("\n" + "=" * 70)
    tree.show("Arvore Rubro-Negra (RedBlackTreeMap)")
    print("=" * 70)
    print("\n3. Acessando valores por chave:")
    test_keys = [44, 17, 97, 28, 76]
    for k in test_keys:
        print(f"   tree[{k}] = {tree[k]}")
    print("\n4. Tentando acessar chave inexistente:")
    try:
        value = tree[99]
    except KeyError as e:
        print(f"   {e}")
    print("\n5. Operacoes posicionais:")
    first_pos = tree.first()
    last_pos = tree.last()
    print(f"   Primeiro: chave={first_pos.key()}, valor={first_pos.value()}")
    print(f"   Ultimo: chave={last_pos.key()}, valor={last_pos.value()}")
    print("\n6. Navegando pela arvore:")
    pos = tree.find_position(32)
    print(f"   Posicao encontrada: chave={pos.key()}, valor={pos.value()}")
    before_pos = tree.before(pos)
    after_pos = tree.after(pos)
    print(f"   Antes: chave={before_pos.key()}, valor={before_pos.value()}")
    print(f"   Depois: chave={after_pos.key()}, valor={after_pos.value()}")
    print("\n7. Operacoes de map ordenado:")
    min_item = tree.find_min()
    print(f"   Minimo: {min_item}")
    ge_item = tree.find_ge(50)
    print(f"   Menor >= 50: {ge_item}")
    print(f"\n   Range [30, 70):")
    for k, v in tree.find_range(30, 70):
        print(f"      {k} -> {v}")
    print("\n8. Iteracao em ordem (inorder traversal):")
    print(f"   Chaves: {list(tree)}")
    print("\n9. Atualizando valor:")
    print(f"   Antes: tree[44] = {tree[44]}")
    tree[44] = "UPDATED"
    print(f"   Depois: tree[44] = {tree[44]}")
    print(f"   (Atualizacao nao afeta o balanceamento)")
    print("\n10. Deletando elementos:")
    delete_keys = [17, 88]
    for k in delete_keys:
        print(f"\n   Deletando chave {k}...")
        del tree[k]
        print(f"   Tamanho apos delecao: {len(tree)}")
        tree.show(f"Apos deletar {k}")
    print("\n12. Tentando deletar chave inexistente:")
    try:
        del tree[99]
    except KeyError as e:
        print(f"   {e}")
    print("\n13. Estado final da arvore:")
    print(f"   Tamanho: {len(tree)}")
    print(f"   Chaves em ordem: {list(tree)}")
    print(f"\n   Todos os pares (chave -> valor e cor):")
    for k in tree:
        pos = tree.find_position(k)
        color = "RED" if tree._is_red(pos) else "BLK"
        print(f"      {k} -> {tree[k]} ({color})")