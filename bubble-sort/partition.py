from typing import MutableSequence


def bubble_sort(data: MutableSequence) -> None:
    """
    Sorts a mutable sequence (eg: list / array) in place (doesn't recreate the data)
    """

    # this is basically going in descending order
    # from the end of the array
    # to the top
    for sorted_partition in range(len(data) - 1, 0, -1):
        for i in range(sorted_partition):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        print(f"End of pass: {sorted_partition}. data is now {data}")


if __name__ == "__main__":
    from array import array

    numbers = array("i", [20, 35, -12, 56, 338, 12, 33, 11, 98, -4])
    print(f"Numbers before sorting: {numbers}")
    bubble_sort(numbers)
    print(f"Numbers after sorting: {numbers}")
