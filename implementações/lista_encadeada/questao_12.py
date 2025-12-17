from src.linked_stack import LinkedStack  # importando da minha própria implementação
from src.linked_queue import LinkedQueue  # importando da minha própria implementação
from src.circular_queue import (
    CircularQueue,
)  # importando da minha própria implementação
from src.linked_deque import LinkedDeque  # importando da minha própria implementação

if __name__ == "__main__":
    print("\nLinkedStack\n")
    l_stack = LinkedStack()
    l_stack.push("Prato de Baixo")
    l_stack.push("Prato de Cima")
    print(f"Topo da pilha: {l_stack.top()}")
    print(f"Desempilhando: {l_stack.pop()}")
    print(f"Novo topo: {l_stack.top()}")

    print("\nLinkedQueue\n")
    l_queue = LinkedQueue()
    l_queue.enqueue("Cliente 01")
    l_queue.enqueue("Cliente 02")
    print(f"Primeiro da fila: {l_queue.first()}")
    print(f"Removendo: {l_queue.dequeue()}")
    print(f"Novo primeiro: {l_queue.first()}")

    print("\nCircularQueue\n")
    c_queue = CircularQueue()
    c_queue.enqueue("Processo A")
    c_queue.enqueue("Processo B")
    c_queue.enqueue("Processo C")
    print(f"Primeiro atual: {c_queue.first()}")
    c_queue.rotate()
    print("...Rotacionando a fila...")
    print(f"Novo primeiro (A foi para o fim): {c_queue.first()}")

    print("\nLinkedDeque\n")
    l_deque = LinkedDeque()
    l_deque.insert_first("Esquerda")
    l_deque.insert_last("Direita")
    print(f"Primeiro: {l_deque.first()}")
    print(f"Último: {l_deque.last()}")
    print(f"Tamanho do deque: {len(l_deque)}")
