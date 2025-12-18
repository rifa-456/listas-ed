from typing import List
from .base import SortAlgorithm, SortResult

class HeapSort(SortAlgorithm):
    def __init__(self):
        self.swaps = None
        self.comparisons = None

    def sort(self, data: List[int]) -> SortResult:
        arr = data.copy()
        n = len(arr)
        self.comparisons = 0
        self.swaps = 0
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.swaps += 1
            self._heapify(arr, i, 0)
        return SortResult(arr, self.comparisons, self.swaps)

    def _heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n:
            self.comparisons += 1
            if arr[l] > arr[largest]:
                largest = l
        if r < n:
            self.comparisons += 1
            if arr[r] > arr[largest]:
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self._heapify(arr, n, largest)