from src.circular_queue import CircularQueue

def count_circular_nodes(c_queue):
    """
    Conta o número de nós em uma lista circularmente encadeada
    acessando a estrutura interna de uma CircularQueue.
    """
    tail = c_queue._tail
    if tail is None:
        return 0
    head = tail._next
    current = head
    count = 1
    while current != tail:
        count += 1
        current = current._next
    return count

if __name__ == "__main__":
    cq = CircularQueue()
    print(f"Lista vazia: {count_circular_nodes(cq)}")
    cq.enqueue(10)
    print(f"1 elemento: {count_circular_nodes(cq)}")
    cq.enqueue(20)
    cq.enqueue(30)
    print(f"3 elementos: {count_circular_nodes(cq)}")
    cq.enqueue(40)
    cq.enqueue(50)
    print(f"5 elementos: {count_circular_nodes(cq)}")
    print(f"Verificação com len(): {len(cq)}")