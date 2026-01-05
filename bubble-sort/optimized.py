# this variant of bubble sort
# is the most optimized
# since it leverages partitioning
# and swapped flag for eartly exit
# this will ensure an early return and skipping additional passes
# this is a quadratic equation

from typing import MutableSequence


def bubble_sort(data: MutableSequence) -> None:
    """
    Sorts a mutable sequence in place.
    Uses partitioning and swapped flag
    """

    for sorted_partition in range(len(data) - 1, 0, -1):
        swapped: bool = False
        for i in range(sorted_partition):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    numbers: list = [34, 221, 76, 43, -2, -7, 100, 46, 122, 98, 334, -65]
    print(f"Numbers before sorting: {numbers}")
    bubble_sort(numbers)
    print(f"Numbers after sorting: {numbers}")
