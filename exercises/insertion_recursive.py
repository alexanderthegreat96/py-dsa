from typing import MutableSequence

# must be implemented in a recusive way
def insertion_sort_recursive(data: MutableSequence, num_items : int) -> None:
    """Sorts a mutable sequence (eg. list or array) in place."""
    if num_items < 2: # this is required to break any recussion loops
        return
    
    num_items -= 1 # reduce the number of items to sort by one
    insertion_sort_recursive(data, num_items) # sort the first num_items items recursively

    new_element = data[num_items] # new element set to data[num_items]
    i = num_items # i is set to num_items
    while i > 0 and data[i - 1] > new_element:
        data[i] = data[i - 1]
        i -= 1

    data[i] = new_element
    print(f"End of pass {num_items}.  `data` is now {data}")


if __name__ == '__main__':
    from array import array

    numbers = [20, 35, -15, 7, 55, 1, -22]

    print(f"Sorting {numbers}")
    insertion_sort_recursive(numbers, len(numbers))
    print(f"The sorted data is {numbers}")