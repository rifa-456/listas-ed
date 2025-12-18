from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class SortResult:
    """Class to hold the result of a sorting operation."""

    sorted_list: List[int]
    comparisons: int
    swaps: int


class SortAlgorithm(ABC):
    """Abstract base class for all sorting algorithms."""

    @abstractmethod
    def sort(self, data: List[int]) -> SortResult:
        """
        Sorts the given list of integers.
        Returns the sorted list, number of comparisons, and number of swaps.
        """
        pass