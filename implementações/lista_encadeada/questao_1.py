from src.array_stack import ArrayStack  # importando da minha própria implementação
from src.array_queue import ArrayQueue  # importando da minha própria implementação
from src.array_deque import ArrayDeque  # importando da minha própria implementação

if __name__ == "__main__":
    print("\n(Stack)\n")
    stack = ArrayStack()
    stack.push("Prato de Baixo")
    stack.push("Prato de Cima")
    print(f"Topo da pilha: {stack.top()}")
    print(f"Desempilhando: {stack.pop()}")
    print(f"Novo topo: {stack.top()}")

    print("\n(Queue)\n")
    queue = ArrayQueue()
    queue.enqueue("Cliente 01")
    queue.enqueue("Cliente 02")
    print(f"Primeiro da fila: {queue.first()}")
    print(f"Removendo: {queue.dequeue()}")
    print(f"Novo primeiro: {queue.first()}")

    print("\n(Deque)\n")
    deque = ArrayDeque()
    deque.add_first("Esquerda")
    deque.add_last("Direita")
    print(f"Primeiro: {deque.first()}")
    print(f"Último: {deque.last()}")
    print(f"Tamanho do deque: {len(deque)}")
