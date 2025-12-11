from src.array_stack import ArrayStack

def reverse_list(L):
    S = ArrayStack()
    for e in L:
        S.push(e)
    for i in range(len(L)):
        L[i] = S.pop()

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(f"Original: {data}")

    reverse_list(data)

    print(f"Revertida: {data}")