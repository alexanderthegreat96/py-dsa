from typing import MutableSequence

def insertion_sort(data:  MutableSequence) -> None:
    """Sorts a mutable sequence in place."""
    
    # traverse from left to right
    for first_unsorted_index in range(1, len(data)):
        # store the firt elemenet
        new_element = data[first_unsorted_index]
       
        # set i to the first index - 1
        i = first_unsorted_index - 1
        # ensure this isn't the first element
        # and that current element is larger than the new element
        while i >= 0 and data[i] > new_element:
            # shift pos to the right
            data[i + 1] = data[i]
            # drecrement i
            i -= 1
        
        # increment the new element to the right
        # and set the new element
        data[i + 1] = new_element

        # print(f'End of pass {first_unsorted_index}. data is now {data}')



if __name__ == "__main__":
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])

    print(f'Numbers before sorting: {numbers}')

    insertion_sort(numbers)

    print(f'Numbers after sorting: {numbers}')
