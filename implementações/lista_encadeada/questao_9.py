from src.array_stack import ArrayStack


def is_operator(c):
    return c in ["+", "-", "*", "/", "^"]


def prefix_to_infix(expression):
    stack = ArrayStack()
    tokens = expression.split()

    for token in reversed(tokens):
        if not is_operator(token):
            stack.push(token)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = f"({op1} {token} {op2})"
            stack.push(temp)

    return stack.pop()


def prefix_to_postfix(expression):
    stack = ArrayStack()
    tokens = expression.split()

    for token in reversed(tokens):
        if not is_operator(token):
            stack.push(token)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = f"{op1} {op2} {token}"
            stack.push(temp)

    return stack.pop()


if __name__ == "__main__":
    expressions = ["* + A B - C D", "+ - 5 2 4", "/ + 3 * 2 4 - 8 6"]

    for expr in expressions:
        print(f"Prefixada:  {expr}")
        print(f"Infixa:   {prefix_to_infix(expr)}")
        print(f"Pós-fixa: {prefix_to_postfix(expr)}")
        print("-" * 30)
