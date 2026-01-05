from typing import MutableSequence

def shell_sort(data:  MutableSequence) -> None:
    """Sorts a mutable sequence in place using the Shell Sort algorithm."""
    n = len(data)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1  # Using Knuth's sequence

    while gap > 0:
        for i in range(gap, n):
            new_element = data[i]
            j = i
            while j >= gap and data[j - gap] > new_element:
                data[j] = data[j - gap]
                j -= gap
            data[j] = new_element
        gap //= 3
        
if __name__ == "__main__":
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])

    print(f'Numbers before sorting: {numbers}')
    shell_sort(numbers)
    print(f'Numbers after sorting: {numbers}')
