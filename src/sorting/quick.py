from typing import List
from .base import SortAlgorithm, SortResult
import sys

class QuickSort(SortAlgorithm):
    def __init__(self):
        self.swaps = None
        self.comparisons = None

    def sort(self, data: List[int]) -> SortResult:
        arr = data.copy()
        self.comparisons = 0
        self.swaps = 0
        self._quick_sort(arr, 0, len(arr) - 1)
        return SortResult(arr, self.comparisons, self.swaps)

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        return i + 1