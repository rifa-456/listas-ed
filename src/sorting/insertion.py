from typing import List
from .base import SortAlgorithm, SortResult


class InsertionSort(SortAlgorithm):
    def sort(self, data: List[int]) -> SortResult:
        arr = data.copy()
        n = len(arr)
        comparisons = 0
        swaps = 0
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0:
                comparisons += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    swaps += 1
                    j -= 1
                else:
                    break
            arr[j + 1] = key
        return SortResult(arr, comparisons, swaps)