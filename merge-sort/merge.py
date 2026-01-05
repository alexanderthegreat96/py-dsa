from typing import MutableSequence

def merge(data : MutableSequence, start: int, mid: int, end: int) -> None:
    """Merge the left and right vaues around mid point of the data"""
    if data[mid - 1] <= data[mid]:
        return

    left_pos : int = start
    right_pos : int = mid
    temp_index: int =  0
    
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

def merge_sort(data: MutableSequence, start: int = 0, end: int = None) -> None:
    """Sorts a mutable sequence"""
    
    if end is None:
        end = len(data)

    if (end - start) < 2:
        return
    
    mid = (start + end) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid, end)
    merge(data, start, mid, end)

if __name__ == "__main__":
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])
    print(f'Numbers before sorting: {numbers}')
    merge_sort(numbers)
    print(f'Numbers after sorting: {numbers}')
