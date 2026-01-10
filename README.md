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

# 🏗️ Data Structures
Data structures are simply ways to organize, well, data.


### 1. Linear Structures
* **Arrays/Lists:** Contiguous memory storage. Best for general-purpose use and index-based access.
* **Singly Linked Lists:** Nodes pointing forward. Best for frequent insertions at the head.
* **Doubly Linked Lists:** Nodes pointing both ways. Best for bidirectional navigation.
* **Stacks (LIFO):** Last-In, First-Out. Best for undo/redo logic and function call management.
* **Queues (FIFO):** First-In, First-Out. Best for task scheduling and processing data in arrival order.

### 2. Nonlinear & Hierarchical Structures
* **Hash Tables (Dictionaries):** Key-Value mapping. Best for instant $O(1)$ lookups and caching.
* **Binary Search Trees (BST):** Sorted hierarchical nodes. Best for maintaining sorted data and $O(\log n)$ searching.
* **Tries (Prefix Trees):** Character-path nodes. Best for autocomplete, spell checkers, and prefix matching.
* **Graphs:** Network of vertices and edges. Best for modeling social networks, maps, and recommendation engines.

---

## 📦 1. Arrays & Dynamic Lists
The most basic data structure. It stores elements in contiguous memory locations.

* **Pros:** Fastest access via index.
* **Cons:** Resizing and inserting in the middle can be slow.
* **Access:** $O(1)$
* **Search:** $O(n)$

```python
# Python lists act as dynamic arrays
my_list = [10, 20, 30, 40]

# Accessing by index (O(1))
element = my_list[2] # 30

# Inserting at the beginning (O(n) because all other items must shift)
my_list.insert(0, 5)
```

## 🔗 2. Singly Linked Lists
A **Singly Linked List** is a linear collection of nodes where each node points to the **next** node in the sequence. The list starts at a **Head** and ends at a node pointing to `None`.

* **Pros:** Dynamic size and efficient $O(1)$ insertions/deletions at the head.
* **Cons:** No random access (you can't jump to index 5) and you can only move in one direction.
* **Access/Search:** $O(n)$
* **Insertion (at Head):** $O(1)$



```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

## 🔗 3. Doubly Linked Lists
A **Doubly Linked List** is a more advanced version of a linked list where each node contains **two** pointers: one to the `next` node and one to the `previous` node.

* **Pros:** Allows for bidirectional traversal (forward and backward) and easier deletion of a node if you already have a reference to it.
* **Cons:** Uses more memory per node to store the extra pointer.
* **Insertion/Deletion:** $O(1)$
* **Search:** $O(n)$

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        # Link the current tail to the new node
        self.tail.next = new_node
        new_node.prev = self.tail
        # Update the tail to the new node
        self.tail = new_node
```
## 🥞 4. Stacks (LIFO)
A **Stack** is a linear data structure that follows the **Last-In, First-Out** principle. The last element added to the stack is the first one to be removed. Think of it like a stack of plates; you only interact with the one on top.

* **Pros:** Extremely fast $O(1)$ operations for adding and removing data.
* **Cons:** No random access; you must remove the top items to reach the bottom.
* **Push (Add):** $O(1)$
* **Pop (Remove):** $O(1)$

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]
```

## 🎟️ 5. Queues (FIFO)
A **Queue** follows the **First-In, First-Out** principle. The first element added is the first one to be removed, identical to a line of people waiting at a store.

* **Pros:** Maintains the exact order of data arrival (First-come, first-served).
* **Cons:** In Python, using a standard `list` for a queue is slow ($O(n)$) because removing the first element requires shifting all other elements.
* **Enqueue (Add to back):** $O(1)$
* **Dequeue (Remove from front):** $O(1)$ (using `deque`)

```python
from collections import deque

class Queue:
    def __init__(self):
        # We use deque (double-ended queue) for O(1) performance
        self.items = deque()

    def enqueue(self, item):
        """Add an item to the end of the line."""
        self.items.append(item)

    def dequeue(self):
        """Remove the item from the front of the line."""
        if len(self.items) == 0:
            return None
        return self.items.popleft()

    def size(self):
        return len(self.items)
```

## 🌲 6. Binary Search Trees (BST)
A **Binary Search Tree** is a hierarchical structure where each node has at most two children. It is organized specifically to allow for fast searching. For any given node:
* The **Left** child contains a value smaller than the parent.
* The **Right** child contains a value larger than the parent.

* **Pros:** Much faster than a linked list for searching and sorting.
* **Cons:** If the tree becomes "unbalanced" (e.g., all nodes added in increasing order), it performs poorly like a linked list ($O(n)$).
* **Search/Insert:** $O(\log n)$ average.



```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self._insert_recursive(current.right, value)
```
## 🔍 7. Tries (Prefix Trees)
A **Trie** (pronounced "try") is an advanced tree-like data structure used for retrieving specific keys from a set, typically strings. Unlike a standard tree, nodes do not store the word itself; instead, their **position** in the tree defines the key they represent.

* **Pros:** Extremely fast for prefix matching and autocomplete. It is more efficient than a Hash Table for looking up words with shared prefixes.
* **Cons:** Can consume a significant amount of memory since every character in every word requires a node.
* **Search/Insert:** $O(L)$ where $L$ is the length of the string.


```python
class TrieNode:
    def __init__(self):
        # Dictionary maps characters to the next TrieNode
        self.children = {}
        # Boolean to track if this node marks the end of a complete word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def starts_with(self, prefix):
        """Returns True if there is any word in the trie that starts with the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
```

## 🕸️ 8. Graphs (Adjacency List)
A **Graph** consists of a set of **Vertices** (nodes) and **Edges** (connections between them). We typically implement them using an **Adjacency List**, which is essentially a dictionary where every node maps to a list of its neighbors.

* **Pros:** Extremely powerful for modeling networks and finding the shortest path between points.
* **Cons:** More complex to traverse; you must track "visited" nodes to avoid infinite loops (cycles).
* **Search (BFS/DFS):** $O(V + E)$ where $V$ is vertices and $E$ is edges.



```python
class Graph:
    def __init__(self):
        # The dictionary key is the node, the value is a list of neighbors
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2, bidirectional=True):
        """Add a connection between two vertices."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        self.adj_list[v1].append(v2)
        if bidirectional:
            self.adj_list[v2].append(v1)

    def get_neighbors(self, vertex):
        return self.adj_list.get(vertex, [])
```

## 🧭 9. Graph Traversal (DFS & BFS)
Unlike linear structures, graphs require specific strategies to visit every node without getting stuck in infinite loops (cycles).

### Depth-First Search (DFS)
DFS goes as deep as possible down one branch before backtracking to the last "fork in the road." It is built using **Recursion** or a **Stack**.
* **Best for:** Detecting cycles, solving mazes, and pathfinding where you need to explore every possibility.


```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(node)
    print(f"DFS Visited: {node}")
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph.adj_list[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### Breadth-First Search (BFS)
BFS explores a graph layer-by-layer. It visits all immediate neighbors first before moving to the neighbors' neighbors. It is built using a **Queue**.

* **Logic:** First-In, First-Out (FIFO).
* **Best for:** Finding the **shortest path** between two nodes in an unweighted network (e.g., finding the fewest number of hops between friends in a social network).

```python
from collections import deque

def bfs(graph, start_node):
    visited = set()
    # Queue stores nodes to visit in the order they were discovered
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        # Pop the oldest node (First-In, First-Out)
        current = queue.popleft()
        print(f"BFS Visited: {current}")
        
        # Check all neighbors of the current node
        for neighbor in graph.adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## 📊 Data Structure Complexity Cheat Sheet

This table summarizes the time complexity for common operations. Understanding these trade-offs is critical for choosing the right structure for your specific problem.

| Data Structure | Access | Search | Insertion | Deletion |
| :--- | :--- | :--- | :--- | :--- |
| **Array (Dynamic)** | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| **Doubly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| **Stack (LIFO)** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| **Queue (FIFO)** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| **Binary Search Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| **Trie (Prefix Tree)** | $O(L)$ | $O(L)$ | $O(L)$ | $O(L)$ |
| **Graph (BFS/DFS)** | N/A | $O(V + E)$ | $O(1)$ | $O(1)$ |

### Key:
* **$n$**: Number of elements in the structure.
* **$L$**: Length of the word/string being searched.
* **$V$**: Number of Vertices (nodes) in a graph.
* **$E$**: Number of Edges (connections) in a graph.
* **Note**: Tree and Graph complexities assume the structures are relatively balanced.