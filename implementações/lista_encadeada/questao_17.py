from src.linked_stack import LinkedStack


def reverse_recursive(node):
    if node is None or node._next is None:
        return node
    new_head = reverse_recursive(node._next)
    node._next._next = node
    node._next = None
    return new_head


def print_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current._element))
        current = current._next
    print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push("D")
    stack.push("C")
    stack.push("B")
    stack.push("A")
    print("Lista Original:")
    print_list(stack._head)
    reversed_head = reverse_recursive(stack._head)
    stack._head = reversed_head
    print("\nLista Invertida:")
    print_list(stack._head)
