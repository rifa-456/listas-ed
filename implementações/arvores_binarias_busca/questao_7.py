from src.red_black_tree_map import RedBlackTreeMap

if __name__ == "__main__":
    tree = RedBlackTreeMap()
    keys_to_insert = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    print(f"Chaves a inserir: {keys_to_insert}")
    print("\n" + "=" * 60)
    for i, key in enumerate(keys_to_insert, 1):
        tree[key] = f"Node({key})"
        print(f"Passo {i}: Inserido {key}")
        print("-" * 60)
        tree.show(f"Estado da Árvore Rubro-Negra após inserir {key}")
        print("=" * 60)
