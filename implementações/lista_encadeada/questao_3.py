from src.array_stack import ArrayStack


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


if __name__ == "__main__":
    S = ArrayStack()
    T = ArrayStack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)

    print(f"dados em S: {S._data}")
    print(f"dados em T: {T._data}")

    transfer(S, T)

    print(f"dados em S: {S._data}")
    print(f"dados em T: {T._data}")
