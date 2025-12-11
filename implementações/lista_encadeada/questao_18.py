from src.linked_queue import LinkedQueue

def split_pos_neg(source_queue):
    """
    Separa uma lista encadeada (fila) em duas:
    uma com números positivos (e zero) e outra com números negativos.
    """
    pos_queue = LinkedQueue()
    neg_queue = LinkedQueue()

    current = source_queue._head

    while current is not None:
        val = current._element
        if val < 0:
            neg_queue.enqueue(val)
        else:
            pos_queue.enqueue(val)
        current = current._next

    return pos_queue, neg_queue

def print_queue(queue):
    elements = []
    current = queue._head
    while current is not None:
        elements.append(str(current._element))
        current = current._next
    print("[" + ", ".join(elements) + "]")

if __name__ == "__main__":
    original = LinkedQueue()
    values = [10, -5, 3, -1, 0, -2, 8, 15, -9]
    for v in values:
        original.enqueue(v)
    print("Lista Original:")
    print_queue(original)
    positives, negatives = split_pos_neg(original)
    print("\nLista de Positivos (>= 0):")
    print_queue(positives)
    print("\nLista de Negativos (< 0):")
    print_queue(negatives)