# Radix Sort is a non-comparative sorting algorithm that sorts data with integer keys
# by grouping keys by the individual digits which share the same significant position and value.
# Unlike Counting Sort, which is limited by the
# range of the largest number, Radix Sort can handle much larger numbers by processing them digit by digit.
# It typically starts from the Least Significant Digit (LSD) and moves toward the most significant,
# using a stable sorting algorithm (usually Counting Sort) as a subroutine for each digit.
# By breaking the numbers down into digits, Radix Sort avoids the memory explosion that would
# happen in Counting Sort if you tried to sort a list containing the number 1,000,000. It
# essentially treats numbers like "strings" of digits, ensuring that by the time it reaches the final
# digit, the entire list is in perfect order. It is highly efficient for large datasets of integers or
# fixed-length strings.

# you're sorting by tens, hundreds, thousands and then units
# counting sort is often used as the sort algorithm for radix sort


from itertools import accumulate
from typing import MutableSequence


def radix_sort(data: MutableSequence[int], radix: int, width: int) -> None:
    """Radix Sort - sort a ``MutableSequence`` of positive integers.

    :param data: The sequence of positive integers (including zero) to sort.
    :param radix: The radix of the values to sort, 10 for decimal, 2 for binary, etc.
    :param width: Each value must contain the same number of digits, its width.
                  That's the theory; in practice (because of the way each digit is
                  extracted) shorter values can be sorted as long as the width of
                  the longest value is passed in here.
    :return:  ``None``, ``data`` is modified to contain its items in sorted order.
              The sorting function used is a stable **Counting Sort**.
    """

    def get_digit(val: int, pos: int, r: int) -> int:
        result = (val // r**pos) % r
        return result

    def get_sign(val: int, *_) -> 0 | 1:
        return 0 if val < 0 else 1

    def radix_counting_sort(
        values: MutableSequence[int], position: int, rad: int, get_digit: callable
    ) -> None:
        """sorts integer values using a stable couting sort"""
        num_values = len(values)
        count_array = [0] * rad

        for value in values:
            count_array[get_digit(value, position, rad)] += 1

        # calculate a prefix sum over the count_array
        count_array[:] = accumulate(count_array)

        output = [0] * num_values
        for value in reversed(values):
            count_index = get_digit(value, position, rad)
            count_array[count_index] -= 1
            output[count_array[count_index]] = value

        # transfer the output
        for index, value in enumerate(output):
            values[index] = value

    # call the radix_counting_sort function
    for p in range(width):
        radix_counting_sort(data, p, radix, get_digit)

    # final sort on the sign
    radix_counting_sort(data, 0, 2, get_sign)


def main():
    # numbers = array('Q', [1330, 8792, 1594, 4725, 4586, 5729])
    numbers: list[int] = [20, -342, 658, 234, -114, 90, -543, -2, 1450]
    print(f"Sorting {numbers}")
    radix_sort(numbers, 10, 4)
    print(numbers)


if __name__ == "__main__":
    from array import array

    main()
