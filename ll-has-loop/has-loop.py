# given a linked list: [1, 2, 3, 4, 5]
# we want to check if this linked list has a loop

# same 2 pointer approach
# slow and fast
# slow moves 1 item at a time
# fast moves 2 items at a time

# slow = head
# fast = slow

# while fast and fast.next
# slow = slow.next
# fast = fast.next.next # two pointer approach here

# having a loop: even number of nodes: slow and fast will point to the same node
# if you have a loop, you essentially have a problem in the code
# both pointers SHOULD NEVER POINT TO THE SAME NODE
# return True or False


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # same thing
    # 2 pointers
    # slow moves one node at a time
    # fast moves 2 nodes at a time
    def has_loop(self) -> bool:
        slow = self.head
        fast = slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # if they both point to the same node
            # then we have a loop
            # aka -> the last node points to the first node
            if slow == fast:
                return True

        return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())  # Returns True


my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
