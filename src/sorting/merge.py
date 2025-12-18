from typing import List
from .base import SortAlgorithm, SortResult

class MergeSort(SortAlgorithm):

    def __init__(self):
        self.swaps = None
        self.comparisons = None

    def sort(self, data: List[int]) -> SortResult:
        arr = data.copy()
        self.comparisons = 0
        self.swaps = 0
        self._merge_sort(arr)
        return SortResult(arr, self.comparisons, self.swaps)

    def _merge_sort(self, arr: List[int]):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            self._merge_sort(L)
            self._merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                self.comparisons += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    self.swaps += 1
                    i += 1
                else:
                    arr[k] = R[j]
                    self.swaps += 1
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                self.swaps += 1
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                self.swaps += 1
                j += 1
                k += 1