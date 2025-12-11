from src.array_queue import ArrayQueue

if __name__ == "__main__":
    queue = ArrayQueue()

    queue.enqueue(5)
    print("enqueue(5)")

    queue.enqueue(3)
    print("enqueue(3)")

    print(f"dequeue() -> {queue.dequeue()}")

    queue.enqueue(2)
    print("enqueue(2)")

    queue.enqueue(8)
    print("enqueue(8)")

    print(f"dequeue() -> {queue.dequeue()}")

    print(f"dequeue() -> {queue.dequeue()}")

    queue.enqueue(9)
    print("enqueue(9)")

    queue.enqueue(1)
    print("enqueue(1)")

    print(f"dequeue() -> {queue.dequeue()}")

    queue.enqueue(7)
    print("enqueue(7)")

    queue.enqueue(6)
    print("enqueue(6)")

    print(f"dequeue() -> {queue.dequeue()}")

    print(f"dequeue() -> {queue.dequeue()}")

    queue.enqueue(4)
    print("enqueue(4)")

    print(f"dequeue() -> {queue.dequeue()}")

    print(f"dequeue() -> {queue.dequeue()}")

    print(f"\nEstado Final: {queue._data}")
    print(f"Tamanho: {len(queue)}")