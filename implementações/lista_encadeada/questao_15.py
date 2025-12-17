from src.linked_stack import LinkedStack


def count_nodes_recursive(node):
    if node is None:
        return 0
    else:
        return 1 + count_nodes_recursive(node._next)


if __name__ == "__main__":
    stack = LinkedStack()
    print(f"Lista vazia - Contagem: {count_nodes_recursive(stack._head)}")
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    stack.push("E")
    print(f"Lista com 5 elementos - Contagem: {count_nodes_recursive(stack._head)}")
    print(f"Len() da stack: {len(stack)}")
