from src.array_stack import ArrayStack

if __name__ == "__main__":

    stack = ArrayStack()

    stack.push(5)
    print("push(5)")

    stack.push(3)
    print("push(3)")

    print(f"pop() -> retorna {stack.pop()}")

    stack.push(2)
    print("push(2)")

    stack.push(8)
    print("push(8)")

    print(f"pop() -> retorna {stack.pop()}")

    print(f"pop() -> retorna {stack.pop()}")

    stack.push(9)
    print("push(9)")

    stack.push(1)
    print("push(1)")

    print(f"pop() -> retorna {stack.pop()}")

    stack.push(7)
    print("push(7)")

    stack.push(6)
    print("push(6)")

    print(f"pop() -> retorna {stack.pop()}")

    print(f"pop() -> retorna {stack.pop()}")

    stack.push(4)
    print("push(4)")

    print(f"pop() -> retorna {stack.pop()}")

    print(f"pop() -> retorna {stack.pop()}")

    print(f"Pilha vazia? {stack.is_empty()}")
    if not stack.is_empty():
        print(f"Topo da pilha: {stack.top()}")
        print(f"Conteúdo interno (base -> topo): {stack._data}")