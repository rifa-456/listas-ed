from src.avl_tree_map import AVLTreeMap

if __name__ == "__main__":
    avl = AVLTreeMap()
    print("\n1. AVLTreeMap criado (vazio)")
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
        (80, "L"),
        (78, "M"),
    ]
    for k, v in items:
        avl[k] = v
        print(f"   Inserido: {k} -> {v}")
    print(f"\n   Tamanho da árvore: {len(avl)}")
    print("\n" + "=" * 60)
    avl.show("Árvore AVL - Auto-Balanceada")
    print("=" * 60)
    print("\n3. Verificando propriedade AVL:")
    print("\n4. Acessando valores por chave:")
    test_keys = [44, 17, 97, 28, 78]
    for k in test_keys:
        print(f"   avl[{k}] = {avl[k]}")

    print("\n5. Tentando acessar chave inexistente:")
    try:
        value = avl[99]
    except KeyError as e:
        print(f"   {e}")

    print("\n6. Operações posicionais:")
    first_pos = avl.first()
    last_pos = avl.last()
    print(f"   Primeiro: chave={first_pos.key()}, valor={first_pos.value()}")
    print(f"   Último: chave={last_pos.key()}, valor={last_pos.value()}")

    print("\n7. Navegando pela árvore AVL:")
    pos = avl.find_position(54)
    print(f"   Posição encontrada: chave={pos.key()}, valor={pos.value()}")
    before_pos = avl.before(pos)
    after_pos = avl.after(pos)
    if before_pos:
        print(f"   Antes: chave={before_pos.key()}, valor={before_pos.value()}")
    if after_pos:
        print(f"   Depois: chave={after_pos.key()}, valor={after_pos.value()}")

    print("\n8. Operações de map ordenado:")
    min_item = avl.find_min()
    print(f"   Mínimo: {min_item}")
    ge_item = avl.find_ge(50)
    print(f"   Menor >= 50: {ge_item}")
    print(f"   Range [30, 70):")
    for k, v in avl.find_range(30, 70):
        print(f"      {k} -> {v}")

    print("\n9. Iteração em ordem (inorder traversal):")
    print("   Chaves:", list(avl))

    print("\n10. Atualizando valor:")
    print(f"   Antes: avl[44] = {avl[44]}")
    avl[44] = "UPDATED"
    print(f"   Depois: avl[44] = {avl[44]}")

    print("\n11. Deletando elementos:")
    print(f"   Deletando chave 17...")
    del avl[17]
    print(f"   Tamanho após deleção: {len(avl)}")

    print("\n" + "=" * 60)
    avl.show("Árvore AVL após deleção de 17")
    print("=" * 60)

    print(f"\n   Deletando chave 88...")
    del avl[88]
    print(f"   Tamanho após deleção: {len(avl)}")
    print("\n" + "=" * 60)
    avl.show("Árvore AVL após deleção de 88")
    print("=" * 60)
    print(f"\n   Deletando chave 65...")
    del avl[65]
    print(f"   Tamanho após deleção: {len(avl)}")
    print("\n" + "=" * 60)
    avl.show("Árvore AVL após deleção de 65")
    print("=" * 60)
    print("\n12. Tentando deletar chave inexistente:")
    try:
        del avl[99]
    except KeyError as e:
        print(f"   {e}")
    print("\n13. Estado final da árvore AVL:")
    print(f"   Tamanho: {len(avl)}")
    print(f"   Chaves em ordem: {list(avl)}")
    print(f"   Todos os pares:")
    for k in avl:
        print(f"      {k} -> {avl[k]}")
    print("\n14. Demonstração de pior caso para BST comum:")
    print("   Inserindo chaves sequenciais [1, 2, 3, 4, 5, 6, 7]")
    avl2 = AVLTreeMap()
    sequential = [(i, f"Val{i}") for i in range(1, 8)]
    for k, v in sequential:
        avl2[k] = v
    print("\n" + "=" * 60)
    avl2.show("AVL com Inserções Sequenciais (1-7)")
    print("=" * 60)
