from src.array_stack import ArrayStack


def is_matched(expression):
    stack = ArrayStack()
    lefty = "({["
    righty = ")}]"

    for c in expression:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()


if __name__ == "__main__":
    expressions = [
        "(5+{(5}) * (4-2)",
        "((5+2) * (8-3))",
        "(5+2",
        ")5+2(",
        "{(5+2) + [3*4]}",
        "{(5+2) + [3*4]",
    ]

    for expr in expressions:
        result = is_matched(expr)
        print(f"Expressão: {expr:<20} | Bem-formatada: {result}")
