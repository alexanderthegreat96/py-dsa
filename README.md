# Sorting Algorithms 
 - `in place sort`:
	 - modifies the original data rather than re-creating and restoring it it's more effective this way
	 - generally, an in-place sorting algorithm doesn't require additional space proportional to the data size
	 - exact definitions may vary
- `stable sort`
	- a stable sorting algorithm keeps equal elements in the same order that they appear in the data. The relative ordering of equal elements is maintained

## Stable vs Unstable Sort Algorithms
  - stable sorts
  - unstable sorts
  - this comes into play when we have duplicate data into the sorting
  - example:
	  - [5, 9, 3, 9, 8, 4]
	  - in an unstable scenario, the order of the Nines will not be preserved
	  - while in a stable scenario, they will be
	  - the first 9 is a blue one
	  - the second 9 is a red one
	  - unstable -> the red one is placed before the blue one
	  - stable -> the blue one is before the red one

## 🫧 Bubble Sort
* **Purpose:** Primarily educational; it is the most intuitive "first step" into sorting logic.
* **Mechanism:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The largest values "bubble up" to the end of the array with each pass.
* **Complexity:**
    * **Time (Worst/Average):** Quadratic $O(n^2)$ due to nested loops.
    * **Time (Best):** $O(n)$ if a `swapped` flag is used and the list is already sorted.
    * **Space:** In-place $O(1)$.
* **Stability:** **Stable**. Duplicate values do not swap past each other, preserving their original relative order.

```python
from typing import MutableSequence

def bubble_sort(data: MutableSequence) -> None:
    """
    Sorts a mutable sequence in place.
    Uses partitioning and swapped flag
    """

    for sorted_partition in range(len(data) - 1, 0, -1):
        swapped: bool = False
        for i in range(sorted_partition):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        if not swapped:
            break
```

---

## 🎯 Selection Sort
* **Purpose:** Useful when memory writes are expensive, as it minimizes the total number of swaps compared to other $O(n^2)$ algorithms.
* **Mechanism:** Divides the list into sorted and unsorted partitions. It "selects" the smallest (or largest) element from the unsorted section and swaps it with the first element of that section.
* **Complexity:**
    * **Time:** Quadratic $O(n^2)$ for all cases (it must scan the unsorted part even if the array is already sorted).
    * **Space:** In-place $O(1)$.
* **Performance:** Generally performs fewer swaps than Bubble Sort but the same number of comparisons.
* **Stability:** **Unstable**. Long-distance swaps can move a duplicate element past another of the same value, changing their original relative order.

```python
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
```

---

## 🃏 Insertion Sort
* **Purpose:** Highly efficient for small datasets or "nearly sorted" arrays. It is often used as the base for more complex hybrid algorithms like Timsort.
* **Mechanism:** Builds the sorted partition one item at a time. It picks the next element from the unsorted side and "inserts" it into the correct position by shifting larger elements to the right.
* **Complexity:**
    * **Time (Worst/Average):** Quadratic $O(n^2)$.
    * **Time (Best):** Linear $O(n)$ (when the array is already sorted).
    * **Space:** In-place $O(1)$.
* **Stability:** **Stable**. It only shifts elements that are strictly greater than the one being inserted, so duplicates stay in their original order.

```python
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

        print(f'End of pass {first_unsorted_index}. data is now {data}')

```

### Version 2
```python
from typing import MutableSequence

def insertion_sort(data: MutableSequence) -> None:
	"""Sorts a mutable sequence in place."""
	for first_unsorted_index in range(1, len(data)):
		new_element = data[first_unsorted_index]
		
		i = first_unsorted_index
		while i > 0 and data[i - 1] > new_element:
			data[i] = data[i - 1]
			i -= 1
		data[i] = new_element
```
---

## 🐚 Shell Sort
* **Purpose:** An optimization of Insertion Sort designed to handle large-scale "shuffling" more efficiently.
* **Mechanism:** It compares elements at a specific distance (called a **gap**). The gap starts large and shrinks over time. Each pass performs a "gap-insertion sort." By the time the gap is 1, the array is almost entirely sorted, making the final pass extremely fast.
* **Complexity:**
    * **Time:** Depends on the gap sequence. Typically ranges from $O(n \log^2 n)$ to $O(n^{1.5})$
    * **Space:** In-place $O(1)$.
* **Performance:** Much faster than Bubble, Selection, or standard Insertion sort for medium-sized arrays.
* **Stability:** **Unstable**. Because elements are compared and swapped over long distances (gaps), the relative order of equal elements is not guaranteed.

```python
from typing import MutableSequence

def shell_sort(data: MutableSequence) -> None:
	"""Sorts a mutable sequence in place using the Shell Sort algorithm."""
	n = len(data)
	gap = 1
	
	# uses the knuth sequence here
	while gap < n // 3:
		gap = gap * 3 + 1
	
	while gap > 0:
		for i in range(gap, n):
			new_element = data[i]
			j = i
			
			while j >= gap and data[j - gap] > new_element:
				data[j] = data[j - gap]
				j -= gap
				
			data[j] = new_element
		
		gap //= 3
```

## 🧩 Merge Sort
* **Purpose:** A highly efficient, general-purpose sorting algorithm that follows the **Divide and Conquer** paradigm.
* **Mechanism:** * **Splitting Phase:** Recursively divides the array into halves until each sub-array contains only one element. A single-element array is base-case sorted.
    * **Merging Phase:** Repeatedly merges sub-arrays back together in the correct order. It uses pointers to compare the smallest available elements of two sorted lists, picking the smaller of the two to build the new sorted list.
* **Complexity:**
    * **Time:** Log-linear $O(n \log n)$ for all cases (Best, Average, and Worst). The "divide" part is logarithmic, while the "merge" part is linear.
    * **Space:** $O(n)$ because it is **not in-place**; it requires temporary arrays to store elements during the merging process.
* **Stability:** **Stable**. During the merge step, if two elements are equal, the algorithm is typically written to pick the element from the "left" side first, preserving their original order.



---

### 🔍 Key Implementation Details
* **Recursive Structure:** The algorithm keeps calling itself on the left and right halves until the base case (array length <= 1) is reached.
* **Merging Logic:** 1. Compare the first element of the `left` sub-array with the first element of the `right`.
    2. Move the smaller element into a temporary array.
    3. Increment the pointer for the array that provided the element.
    4. Once one sub-array is empty, copy all remaining elements from the other sub-array into the temporary array.
* **Trade-offs:** While much faster than Bubble or Insertion sort for large datasets, the $O(n)$ space requirement can be a drawback if memory is extremely limited.
```python
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
```

## ⚡ Quick Sort
- **Divide and Conquer:** Picks a "pivot" element and partitions the array into elements smaller than the pivot and elements larger than the pivot.
- **In-Place:** Unlike Merge Sort, it doesn't require extra arrays for the merging phase, making it memory efficient.
- **Complexity:**
    - **Average Time:** $O(n \log n)$ — extremely fast for most real-world data.
    - **Worst Case:** $O(n^2)$ — occurs when the pivot is consistently the smallest or largest element (e.g., sorting an already sorted array using the first element as the pivot).
- **Stability:** **Unstable** — duplicate values may not retain their original relative positions because of the long-distance swaps across the pivot.
- **Implementation Detail:** Using a middle element or a random element as the pivot helps prevent the $O(n^2)$ worst-case scenario.
```python
from typing import MutableSequence

def quick_sort(data: MutableSequence) -> None:
    """Sorts a mutable sequence in place"""
    _quick_sort(data, 0, len(data) - 1)

def _quick_sort(data: MutableSequence, start: int, end: int):
    # Only sort if there is more than one element
    if start < end:
        # Using the middle element as pivot is safer for sorted/nearly sorted data
        pivot = data[(start + end) // 2] # hoare partition style
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
```

## 🧮 Counting Sort
* **Purpose:** A non-comparative sorting algorithm used for sorting integers within a specific, limited range.
* **Mechanism:** 1. **Count:** Create a "counting array" where the index represents the value and the value represents the frequency.
    2. **Accumulate:** Transform the counting array into a prefix sum array to determine the starting position of each element in the output.
    3. **Place:** Iterate through the input array and place elements into their correct positions in a temporary output array.
* **Complexity:**
    * **Time:** Linear $O(n + k)$, where $n$ is the number of elements and $k$ is the range of the input.
    * **Space:** $O(n + k)$ because it requires an auxiliary counting array and an output array.
* **Stability:** **Stable**. By iterating through the input array in reverse during the "Place" step, it preserves the relative order of duplicate elements.
* **Constraints:** Only works for integers (or data that can be mapped to a discrete range) and is inefficient if the range $k$ is much larger than $n$.

```python
from typing import List

def counting_sort(data: List[int]) -> List[int]:
    """
    Sorts a list of integers using Counting Sort.
    Note: This is not in-place (returns a new sorted list).
    """
    if not data:
        return data

    # 1. Find the range of the input
    max_val = max(data)
    min_val = min(data)
    range_of_elements = max_val - min_val + 1
    
    # 2. Initialize the counting array with zeros
    # This array stores the frequency of each number
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(data)

    # 3. Store the count of each element
    # Use (x - min_val) to handle negative numbers
    for x in data:
        count_arr[x - min_val] += 1

    # 4. Change count_arr[i] so that it contains the actual
    # position of this element in the output array (Cumulative Count)
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # 5. Build the output array
    # We iterate backwards to maintain 'Stability'
    for i in range(len(data) - 1, -1, -1):
        current_val = data[i]
        position = count_arr[current_val - min_val] - 1
        output_arr[position] = current_val
        count_arr[current_val - min_val] -= 1

    return output_arr

if __name__ == "__main__":
    numbers = [4, 2, 2, 8, 3, 3, 1]
    print(f"Before: {numbers}")
    sorted_numbers = counting_sort(numbers)
    print(f"After:  {sorted_numbers}")
```

## 🔢 Radix Sort
* **Purpose:** Efficiently sorts large integers or strings by processing individual digits or characters.
* **Mechanism:** 1. **Digit Extraction:** It looks at the digits of each number starting from the Least Significant Digit (LSD).
    2. **Stable Sub-sort:** It uses a stable sort (like Counting Sort) to sort the numbers based on the current digit.
    3. **Iteration:** It moves to the next digit (tens, hundreds, etc.) and repeats the process until the Most Significant Digit is reached.
* **Complexity:**
    * **Time:** $O(d \cdot (n + k))$, where $d$ is the number of digits, $n$ is the number of elements, and $k$ is the base (usually 10 for decimals).
    * **Space:** $O(n + k)$ for the auxiliary arrays used by the counting sort subroutine.
* **Stability:** **Stable**. It relies on a stable sub-sort to ensure that the relative order from previous digit-passes is preserved.
* **Constraints:** Requires data that can be decomposed into "digits" or "keys" with a lexicographical order.

```python
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
```
### 📊 Comparison Summary

| Algorithm | Best Case | Worst Case | Space | Stability | Key Benefit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble** | O(n) | O(n²) | O(1) | Stable | Simple to detect a sorted list early. |
| **Selection** | O(n²) | O(n²) | O(1) | Unstable | Minimizes total number of swaps. |
| **Insertion** | O(n) | O(n²) | O(1) | Stable | Fastest for small or nearly-sorted data. |
| **Shell** | O(n log n) | O(n²) | O(1) | Unstable | Faster than insertion; great for medium data. |
| **Merge** | O(n log n) | O(n log n) | O(n) | Stable | Reliable, consistent performance; stable. |
| **Quick** | O(n log n) | O(n²) | O(log n) | Unstable | Usually the fastest in-place comparison sort. |
| **Counting** | O(n + k) | O(n + k) | O(n + k) | Stable | Non-comparative; linear time for small ranges. |
| **Radix** | O(nk) | O(nk) | O(n + k) | Stable | Linear time for large integers/fixed-length keys. |

---

### 💡 Legend
* **n**: Number of elements in the array.
* **k**: Range of the values (for Counting Sort).
* **d / k**: Number of digits or the radix (for Radix Sort).
* **Space**: O(1) means "In-Place" (no extra memory).
 