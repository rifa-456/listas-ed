from src.tree_map import TreeMap

if __name__ == "__main__":
    tree = TreeMap()
    print("\n1. TreeMap criado (vazio)")
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
    ]
    for k, v in items:
        tree[k] = v
        print(f"   Inserido: {k} -> {v}")
    print(f"\n   Tamanho da árvore: {len(tree)}")
    print("\n" + "=" * 60)
    tree.show("Árvore Binária de Busca (TreeMap)")
    print("=" * 60)
    print("\n3. Acessando valores por chave:")
    test_keys = [44, 17, 97, 28]
    for k in test_keys:
        print(f"   tree[{k}] = {tree[k]}")
    print("\n4. Tentando acessar chave inexistente:")
    try:
        value = tree[99]
    except KeyError as e:
        print(f"   {e}")
    print("\n5. Operações posicionais:")
    first_pos = tree.first()
    last_pos = tree.last()
    print(f"   Primeiro: chave={first_pos.key()}, valor={first_pos.value()}")
    print(f"   Último: chave={last_pos.key()}, valor={last_pos.value()}")
    print("\n6. Navegando pela árvore:")
    pos = tree.find_position(32)
    print(f"   Posição encontrada: chave={pos.key()}, valor={pos.value()}")
    before_pos = tree.before(pos)
    after_pos = tree.after(pos)
    print(f"   Antes: chave={before_pos.key()}, valor={before_pos.value()}")
    print(f"   Depois: chave={after_pos.key()}, valor={after_pos.value()}")
    print("\n7. Operações de map ordenado:")
    min_item = tree.find_min()
    print(f"   Mínimo: {min_item}")
    ge_item = tree.find_ge(50)
    print(f"   Menor >= 50: {ge_item}")
    print(f"   Range [30, 70):")
    for k, v in tree.find_range(30, 70):
        print(f"      {k} -> {v}")
    print("\n8. Iteração em ordem (inorder traversal):")
    print("   Chaves:", list(tree))
    print("\n9. Atualizando valor:")
    print(f"   Antes: tree[44] = {tree[44]}")
    tree[44] = "UPDATED"
    print(f"   Depois: tree[44] = {tree[44]}")
    print("\n10. Deletando elementos:")
    print(f"   Deletando chave 17...")
    del tree[17]
    print(f"   Tamanho após deleção: {len(tree)}")
    print("\n" + "=" * 60)
    tree.show("Árvore após deleção de 17")
    print("=" * 60)
    print(f"\n   Deletando chave 88...")
    del tree[88]
    print(f"   Tamanho após deleção: {len(tree)}")
    print("\n" + "=" * 60)
    tree.show("Árvore após deleção de 88")
    print("=" * 60)
    print("\n11. Tentando deletar chave inexistente:")
    try:
        del tree[99]
    except KeyError as e:
        print(f"   {e}")
    print("\n12. Estado final da árvore:")
    print(f"   Tamanho: {len(tree)}")
    print(f"   Chaves em ordem: {list(tree)}")
    print(f"   Todos os pares:")
    for k in tree:
        print(f"      {k} -> {tree[k]}")