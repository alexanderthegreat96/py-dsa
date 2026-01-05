# finding the kth node from end

# k -> variable obv

# [1, 2, 3, 4, 5]
# kth from the end
# 1 from the end is 5
# 2 from the end is 4
# etc

# return a pointer to that node basically

# using a fast and slow pointer


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


# will use the linked list
# grab it's head and iterate
# what should happen is this:
# move the fast pointer one step ahead of the slow pointer
# ensure it hits None at the end
# when that happens
# we then exit the for loop
# we simply do a regular while loop
# and we move both fast and slow at the same pace
# slow will essentially have the


def find_kth_from_end(ll: LinkedList, k: int):
    # bound checking
    if k < 0:
        return None

    # fast and slow
    slow = ll.head
    fast = slow

    # we gotta move the fast pointer ahead
    # k times
    for i in range(k):
        if fast is None:
            return

        fast = fast.next

    # we gotta move the slow and fast pointers
    # at the same rate
    # since fast will hit none
    # then slow will stop exacly where fast did

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
