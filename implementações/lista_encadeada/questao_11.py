from src.array_stack import ArrayStack
from src.array_queue import ArrayQueue


def is_palindrome(text):
    stack = ArrayStack()
    queue = ArrayQueue()
    clean_text = "".join(ch.lower() for ch in text if ch.isalnum())

    for char in clean_text:
        stack.push(char)
        queue.enqueue(char)

    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            return False

    return True


if __name__ == "__main__":
    test_strings = [
        "arara",
        "osso",
        "Anotaram a data da maratona",
        "Socorram me subi no onibus em Marrocos",
        "Python",
        "12321",
        "123 45",
    ]

    for s in test_strings:
        result = is_palindrome(s)
        print(f"String: '{s}' -> Palíndromo? {result}")
