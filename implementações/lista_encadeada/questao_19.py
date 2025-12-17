from src.linked_deque import LinkedDeque


def remove_duplicates(deque):
    """
    Remove elementos duplicados de uma lista duplamente encadeada (LinkedDeque).
    Usa um conjunto (set) para rastrear elementos vistos.
    """
    if deque.is_empty():
        return

    seen = set()
    current = deque._header._next
    while current != deque._trailer:
        next_node = current._next
        if current._element in seen:
            deque._delete_node(current)
        else:
            seen.add(current._element)
        current = next_node


def print_deque(deque):
    elements = []
    current = deque._header._next
    while current != deque._trailer:
        elements.append(str(current._element))
        current = current._next
    print("[" + " <-> ".join(elements) + "]")


if __name__ == "__main__":
    dll = LinkedDeque()
    data = [10, 20, 10, 30, 20, 40, 10, 50]
    for x in data:
        dll.insert_last(x)
    print("Lista Original com duplicatas:")
    print_deque(dll)
    print(f"Tamanho: {len(dll)}")
    remove_duplicates(dll)
    print("\nLista após remover duplicatas:")
    print_deque(dll)
    print(f"Tamanho: {len(dll)}")
