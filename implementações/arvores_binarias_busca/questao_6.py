from src.avl_tree_map import AVLTreeMap

if __name__ == "__main__":
    tree = AVLTreeMap()
    initial_keys = [62, 44, 78, 17, 50, 88, 48, 54]
    print(f"Construindo a árvore inicial com as chaves: {initial_keys}")
    print("\n" + "=" * 60)
    for key in initial_keys:
        tree[key] = f"Node({key})"
    tree.show("Estado Inicial (Figura 11.14b)")
    key_to_remove = 62
    print("\n" + "=" * 60)
    print(f"Passo Final: Removendo chave {key_to_remove}")
    print("-" * 60)
    del tree[key_to_remove]
    tree.show(f"Estado da Árvore após remover {key_to_remove}")
    print("=" * 60)
