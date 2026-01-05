from typing import MutableSequence


# only works with non-negative integers
# cannot sort strings or floats
# time complexity O(n + k) where k is the range of the input
def counting_sort(data: MutableSequence[int], min: int, max: int) -> None:
    """Sorts a mutable sequence of non-negative integers in place using Counting Sort."""
    if not data:
        return

    # create a count array
    # size of the range of the input values
    count_array = [0] * (max - min + 1)

    # count the occurrences of each value in the input data
    for val in data:
        count_array[val - min] += 1

    data_index = 0
    # reconstruct the sorted data
    for i, count in enumerate(count_array):
        for _ in range(count):  # loop count times
            data[data_index] = i + min
            data_index += 1


if __name__ == "__main__":
    from array import array

    numbers = array("Q", [20, 35, 15, 7, 55, 1, 22])

    print(f"Numbers before sorting: {numbers}")

    counting_sort(numbers, min(numbers), max(numbers))

    print(f"Numbers after sorting: {numbers}")
