from typing import MutableSequence, Sequence
import logging

logger = logging.getLogger('merge_sort')
logging.basicConfig(filename='merge_sort.log', level=logging.DEBUG, filemode='w')


def merge(data: MutableSequence, start: int, mid: int, end: int) -> None:
    """Merge the left and right values around the ``mid`` point of ``data``."""

    if data[mid - 1] <= data[mid]:
        return

    left_pos = start
    right_pos = mid
    temp_index = 0

    temp = list([0] * (end - start))
    while (left_pos < mid) and (right_pos < end):
        if data[left_pos] <= data[right_pos]:
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


def merge_sort(data: MutableSequence, start: int = 0, end: int = None, indent_level=-1) -> None:
    """Sorts a mutable sequence (eg. list or array) in place."""
    indent_level += 1
    tabs = '\t' * indent_level
    logger.debug(f'{tabs}Recursive call level {indent_level} with data {data[start:end]}. {start=}, {end=}')
    # The function can be called with only the data.
    if end is None:
        end = len(data)

    if (end - start) < 2:
        return

    mid = (start + end) // 2
    merge_sort(data, start, mid, indent_level)
    merge_sort(data, mid, end, indent_level)
    logger.debug(f'{tabs}\t*** merging {data[start:mid]} with {data[mid:end]}')
    merge(data, start, mid, end)
    logger.debug(f'{tabs}\t*** The two merged arrays become {data[start:end]}')


if __name__ == '__main__':
    numbers = [20, 35, -15, 7, 55, 1, -22]

    logger.info(f"Sorting {numbers}")
    print(f"Sorting {numbers}")
    merge_sort(numbers)
    logger.info(f"The sorted data is {numbers}")
    print(f"The sorted data is {numbers}")
