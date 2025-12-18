from typing import List, Type
from src.sorting import (
    SortAlgorithm,
    BubbleSort,
    SelectionSort,
    InsertionSort,
    ShellSort,
    MergeSort,
    QuickSort,
    HeapSort,
    CountingSort,
)
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

dataset = [
    [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
    [100, 48, 19, 61, 86, 33, 13, 43, 84, 28],
    [81, 60, 6, 49, 40, 41, 38, 64, 44, 36],
    [45, 27, 11, 89, 63, 39, 9, 58, 52, 17],
    [88, 77, 26, 62, 30, 96, 56, 65, 98, 99],
    [76, 73, 16, 95, 35, 87, 68, 69, 51, 92],
    [37, 75, 90, 82, 8, 18, 23, 93, 57, 10],
    [15, 97, 14, 29, 7, 24, 31, 59, 78, 85],
    [5, 70, 55, 91, 47, 72, 2, 20, 34, 74],
    [50, 66, 32, 22, 54, 79, 21, 1, 80, 46],
]


def run_benchmark(
    dataset: List[List[int]], algorithms: List[Type[SortAlgorithm]]
) -> List[dict]:
    results = []
    for algo_class in algorithms:
        algo_instance = algo_class()
        algo_name = algo_class.__name__
        total_comparisons = 0
        total_swaps = 0
        for data_row in dataset:
            res = algo_instance.sort(data_row.copy())
            total_comparisons += res.comparisons
            total_swaps += res.swaps
        results.append(
            {
                "name": algo_name,
                "comparisons": total_comparisons,
                "swaps": total_swaps,
                "avg_comp": total_comparisons / len(dataset),
                "avg_swaps": total_swaps / len(dataset),
            }
        )
    return results


def display_results(results: List[dict]):
    console = Console(width=300)
    table = Table(
        title="[bold magenta]Benchmark de Algoritmos de Ordenação[/bold magenta]",
        box=box.ROUNDED,
        header_style="bold cyan",
        expand=False,
    )
    table.add_column(
        "Algoritmo", style="dim", width=20, no_wrap=True, overflow="ignore"
    )
    table.add_column(
        "Complexidade (Méd)",
        justify="center",
        width=25,
        no_wrap=True,
        overflow="ignore",
    )
    table.add_column(
        "Total de Comparações",
        justify="right",
        width=22,
        no_wrap=True,
        overflow="ignore",
    )
    table.add_column(
        "Total de Trocas", justify="right", width=15, no_wrap=True, overflow="ignore"
    )
    table.add_column(
        "Média Comparações",
        justify="right",
        style="green",
        width=20,
        no_wrap=True,
        overflow="ignore",
    )
    table.add_column(
        "Média Trocas",
        justify="right",
        style="yellow",
        width=15,
        no_wrap=True,
        overflow="ignore",
    )

    complexity_map = {
        "InsertionSort": "O(n²)",
        "SelectionSort": "O(n²)",
        "BubbleSort": "O(n²)",
        "ShellSort": "O(n log n) - O(n²)",
        "MergeSort": "O(n log n)",
        "QuickSort": "O(n log n)",
        "HeapSort": "O(n log n)",
        "CountingSort": "O(n+k)",
    }

    for res in results:
        name = res["name"]
        c_hint = complexity_map.get(name, "?")
        table.add_row(
            name,
            c_hint,
            f"{res['comparisons']:,}",
            f"{res['swaps']:,}",
            f"{res['avg_comp']:.1f}",
            f"{res['avg_swaps']:.1f}",
        )

    console.print("\n")
    console.print(table)
    console.print("\n")


def main():
    algorithms = [
        InsertionSort,
        SelectionSort,
        BubbleSort,
        ShellSort,
        MergeSort,
        QuickSort,
        HeapSort,
        CountingSort,
    ]
    results = run_benchmark(dataset, algorithms)
    display_results(results)

if __name__ == "__main__":
    main()