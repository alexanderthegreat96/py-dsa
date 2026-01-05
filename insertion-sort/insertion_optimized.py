from typing import MutableSequence

def insertion_sort(data:  MutableSequence) -> None:
    """Sorts a mutable sequence in place."""
    for first_unsorted_index in range(1, len(data)):
        new_element = data[first_unsorted_index]

        i = first_unsorted_index
        while i > 0 and data[i - 1] > new_element:
            data[i] = data[i - 1]
            i -= 1
        
        data[i] = new_element


if __name__ == "__main__":
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])

    print(f'Numbers before sorting: {numbers}')

    insertion_sort(numbers)

    print(f'Numbers after sorting: {numbers}')
