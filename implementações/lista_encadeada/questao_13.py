from src.linked_stack import LinkedStack


def find_penultimate_node(head):
    """
    Encontra o penúltimo nó em uma lista encadeada simples.
    Retorna o nó, ou None se a lista tiver menos de 2 elementos.
    """
    if head is None or head._next is None:
        return None
    current = head
    while current._next._next is not None:
        current = current._next

    return current


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    print("Estrutura da Lista: D -> C -> B -> A -> None")
    penultimate = find_penultimate_node(stack._head)
    if penultimate:
        print(f"Penúltimo nó encontrado (elemento): {penultimate._element}")
    else:
        print("Não foi possível encontrar o penúltimo nó (lista muito pequena).")
    stack2 = LinkedStack()
    stack2.push("1")
    stack2.push("2")
    print("\nEstrutura da Lista: 2 -> 1 -> None")
    pen2 = find_penultimate_node(stack2._head)
    print(f"Penúltimo nó encontrado (elemento): {pen2._element}")
