from typing import MutableSequence

def quick_sort(data: MutableSequence) -> None:
    """Sorts a mutable sequence in place"""
    _quick_sort(data, 0, len(data) - 1)

def _quick_sort(data: MutableSequence, start: int, end: int):
    # Only sort if there is more than one element
    if start < end:
        # Using the middle element as pivot is safer for sorted/nearly sorted data
        pivot = data[(start + end) // 2]
        i, j = start, end
        
        while i <= j:
            # Move i right while data[i] < pivot
            while data[i] < pivot:
                i += 1
            
            # Move j left while data[j] > pivot
            while data[j] > pivot:
                j -= 1

            if i <= j:
                # Swap elements at i and j
                if i != j:
                    data[i], data[j] = data[j], data[i]
                
                # Move pointers past each other
                i += 1
                j -= 1

        # Recursively process the two halves created by the crossed pointers
        if start < j:
            _quick_sort(data, start, j)
        if i < end:
            _quick_sort(data, i, end)

if __name__ == "__main__":
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])
    #numbers = [20, 35, -15, 7, 55, 1, -22]
    print(f'Numbers before sorting: {numbers}')
    quick_sort(numbers)
    print(f'Numbers after sorting: {numbers}')
