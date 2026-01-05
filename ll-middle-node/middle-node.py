# find the middle node

# given a linked list: [1, 2, 3, 4, 5]
# we are tasked with finding the middle node
# the catch: the linked list does not have a length attribute

# you cannot count the nodes
# not allowed to calculate the length of the list
# can only loop over the list one time only

# the strategy:
# - 2 variables:  slow and fast -> set them equal to head
# - as we iterate, we move fast up 2 and slow up 1


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

    # two pointer approach here
    def find_middle_node(self):
        slow = self.head  # set to the head
        fast = slow  # also set to head via slow

        while fast and fast.next:
            slow = slow.next  # one node at a time
            fast = fast.next.next  # 2 nodes at a time

            # when fast moves out of the nodes
            # or runs out of nodes basically
            # it stops the loop
            # this will return the middle node
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
