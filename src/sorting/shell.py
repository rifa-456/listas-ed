from typing import List
from .base import SortAlgorithm, SortResult


class ShellSort(SortAlgorithm):
    def sort(self, data: List[int]) -> SortResult:
        arr = data.copy()
        n = len(arr)
        comparisons = 0
        swaps = 0
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i

                while j >= gap:
                    comparisons += 1
                    if arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        swaps += 1
                        j -= gap
                    else:
                        break

                arr[j] = temp
            gap //= 2
        return SortResult(arr, comparisons, swaps)