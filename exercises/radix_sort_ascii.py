from itertools import accumulate
from typing import MutableSequence

def radix_sort_strings(data: MutableSequence[str], radix: int, width: int) -> None:
    
    # 1. New helper to get ASCII value at a specific position
    def get_ascii_char(val: str, pos: int, r: int) -> int:
        """
        Calculates the character index from the RIGHT.
        Radix sort must process from Least Significant Digit (right) 
        to Most Significant Digit (left).
        """
        # String indices are left-to-right, so we invert 'pos'
        # e.g., if width is 5 and pos is 0, we want index 4
        string_idx = width - 1 - pos
        
        if string_idx < len(val):
            return ord(val[string_idx])
        return 0  # Padding for shorter strings

    def radix_counting_sort(values: MutableSequence[str], position: int, rad: int, key: callable) -> None:
        num_items = len(values)
        count_array = [0] * rad

        for value in values:
            # We use the ASCII code as the bucket index
            idx = key(value, position, rad)
            count_array[idx] += 1

        count_array[:] = list(accumulate(count_array))

        output = [None] * num_items
        for value in reversed(values):
            count_index = key(value, position, rad)
            count_array[count_index] -= 1
            output[count_array[count_index]] = value

        data[:] = output[:]

    # 2. Main loop: Sort by each character position
    # Width 5 means we go from pos 0 (rightmost char) to 4 (leftmost char)
    for p in range(width):
        radix_counting_sort(data, p, radix, get_ascii_char)

def main():
    # Use radix 256 to safely cover all standard ASCII characters
    strings = ['bdcef', 'dbaqc', 'abcde', 'omadd', 'bbbbb']
    radix_sort_strings(strings, 256, 5)
    print(strings)

if __name__ == '__main__':
    main()