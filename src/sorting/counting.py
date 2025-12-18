from typing import List
from .base import SortAlgorithm, SortResult


class CountingSort(SortAlgorithm):
    def sort(self, data: List[int]) -> SortResult:
        if not data:
            return SortResult([], 0, 0)
        arr = data.copy()
        max_val = arr[0]
        comparisons = 0
        swaps = 0
        for x in arr:
            comparisons += 1
            if x > max_val:
                max_val = x
        count = [0] * (max_val + 1)
        for x in arr:
            count[x] += 1
        index = 0
        for i in range(max_val + 1):
            while count[i] > 0:
                arr[index] = i
                swaps += 1
                index += 1
                count[i] -= 1
        return SortResult(arr, comparisons, swaps)