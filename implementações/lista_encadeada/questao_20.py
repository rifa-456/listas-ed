from src.linked_deque import LinkedDeque

def print_deque(deque, label):
    elements = []
    if not deque.is_empty():
        current = deque._header._next
        while current != deque._trailer:
            elements.append(str(current._element))
            current = current._next

    print(f"{label}: [" + " <-> ".join(elements) + "]")

if __name__ == "__main__":
    dq = LinkedDeque()
    dq.insert_last("A")
    dq.insert_last("B")
    dq.insert_last("C")
    dq.insert_last("D")
    print("--- Estado Inicial ---")
    print_deque(dq, "Original")
    print(f"First: {dq.first()}")
    print(f"Last:  {dq.last()}")
    dq.reverse()
    print("\n--- Após reverse() ---")
    print_deque(dq, "Invertida")
    print(f"First: {dq.first()}")
    print(f"Last:  {dq.last()}")
    print("\n--- Testando operações adicionais ---")
    dq.insert_last("E")
    dq.insert_first("Z")
    print_deque(dq, "Final")