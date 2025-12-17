from src.tree_map import TreeMap

if __name__ == "__main__":
    tree = TreeMap()
    keys_to_insert = [30, 40, 24, 58, 48, 26, 11, 13]
    print(f"Chaves a inserir: {keys_to_insert}")
    print("\n" + "=" * 60)
    for i, key in enumerate(keys_to_insert, 1):
        tree[key] = f"Node({key})"
        print(f"Passo {i}: Inserido {key}")
        print("-" * 60)
        tree.show(f"Estado da Árvore após inserir {key}")
        print("=" * 60)