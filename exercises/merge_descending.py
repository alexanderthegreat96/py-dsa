from typing import MutableSequence

# Merge sort implementation that sorts in descending order
def merge(data: MutableSequence, start: int, mid: int, end: int) -> None:
    """Merge the left and right values around the ``mid`` point of ``data``."""
    if data[mid - 1] >= data[mid]: # changed this line here for descending order
        return

    left_pos = start
    right_pos = mid
    temp_index = 0

    temp = list([0] * (end - start))
    
    while (left_pos < mid) and (right_pos < end):
        if data[left_pos] >= data[right_pos]: # changed this line here for descending order
            temp[temp_index] = data[left_pos]
            left_pos += 1
        else:
            temp[temp_index] = data[right_pos]
            right_pos += 1

        temp_index += 1

    length = mid - left_pos
    for i in range(length):
        data[start + temp_index + i] = data[left_pos + i]
    for i in range(temp_index):
        data[start + i] = temp[i]


def merge_sort(data: MutableSequence, start: int = 0, end: int = None) -> None:
    """Sorts a mutable sequence (eg. list or array) in place."""

    # The function can be called with only the data.
    if end is None:
        end = len(data)

    if (end - start) < 2:
        return


    mid = (start + end) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid, end)
    merge(data, start, mid, end)


if __name__ == '__main__':
    from array import array

    # numbers = [20, 35, -15, 7, 55, 1, -22]
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])

    print(f"Sorting {numbers}")
    merge_sort(numbers)
    print(f"The sorted data is {numbers}")
