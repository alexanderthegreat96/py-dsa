from typing import MutableSequence

def selection_sort(data: MutableSequence) -> None:
    """
    Sorts a mutable sequence in place using selection sort algorithm.
    """

    for last_unsorted_index in range(len(data) - 1, 0, -1):
        largest = 0
        for i in range(1, last_unsorted_index + 1):
            if data[i] > data[largest]:
                largest = i

        
        data[largest], data[last_unsorted_index] = data[last_unsorted_index], data[largest]
        
        # print("End of pass: {last_unsorted_index}. `data` is not {data}")


if __name__ == "__main__":
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])

    print(f'Numbers before sorting: {numbers}')

    selection_sort(numbers)

    print(f'Numbers after sorting: {numbers}')

