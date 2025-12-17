from src.avl_tree_map import AVLTreeMap

if __name__ == "__main__":
    tree = AVLTreeMap()
    initial_keys = [62, 44, 78, 17, 50, 88, 48, 54]
    print(f"Construindo a árvore inicial com as chaves: {initial_keys}")
    print("\n" + "=" * 60)
    for key in initial_keys:
        tree[key] = f"Node({key})"
    tree.show("Estado Inicial")
    key_to_insert = 52
    print("\n" + "=" * 60)
    print(f"Passo Final: Inserindo chave {key_to_insert}")
    print("-" * 60)
    tree[key_to_insert] = f"Node({key_to_insert})"
    tree.show(f"Estado da Árvore após inserir {key_to_insert}")
    print("=" * 60)
