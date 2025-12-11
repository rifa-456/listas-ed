from src.array_deque import ArrayDeque

if __name__ == "__main__":
    deque = ArrayDeque()

    deque.add_first(4)
    print("add_first(4)")

    deque.add_last(8)
    print("add_last(8)")

    deque.add_last(9)
    print("add_last(9)")

    deque.add_first(5)
    print("add_first(5)")

    print(f"last() -> {deque.last()}")

    print(f"delete_first() -> {deque.delete_first()}")

    print(f"delete_last() -> {deque.delete_last()}")

    deque.add_last(7)
    print("add_last(7)")

    print(f"first() -> {deque.first()}")

    print(f"last() -> {deque.last()}")

    deque.add_last(6)
    print("add_last(6)")

    print(f"delete_first() -> {deque.delete_first()}")

    print(f"delete_first() -> {deque.delete_first()}")

    print(f"\nEstado Final: {deque._data}")
    print(f"Tamanho: {len(deque)}")