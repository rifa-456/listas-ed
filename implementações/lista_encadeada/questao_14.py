from src.linked_stack import LinkedStack


def concatenate_lists(head_L, head_M):
    if head_L is None:
        return head_M
    current = head_L
    while current._next is not None:
        current = current._next
    current._next = head_M
    return head_L


def print_list(head):
    current = head
    elements = []
    while current is not None:
        elements.append(str(current._element))
        current = current._next
    print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    L = LinkedStack()
    L.push("C")
    L.push("B")
    L.push("A")
    M = LinkedStack()
    M.push("F")
    M.push("E")
    M.push("D")
    print("Lista L original:")
    print_list(L._head)
    print("\nLista M original:")
    print_list(M._head)
    new_head = concatenate_lists(L._head, M._head)
    print("\nLista Concatenada (L + M):")
    print_list(new_head)
