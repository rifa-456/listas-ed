from src.array_stack import ArrayStack

def recursive_empty(S):
    if S.is_empty():
        return
    S.pop()
    recursive_empty(S)

if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print(f"Pilha antes: {stack._data}")
    print(f"Esta vazia? {stack.is_empty()}")

    recursive_empty(stack)

    print(f"Pilha antes: {stack._data}")
    print(f"Esta vazia? {stack.is_empty()}")