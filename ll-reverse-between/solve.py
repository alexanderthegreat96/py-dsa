# reverse between
# given a linked list
# 1, 2, 3, 4, 5
# indexes ranging from 0 to 4

# we gotta reverse between indexes 3 and 1 -> or list nodes: 2, 3, 4

# the idea is to actually:
# reverse 2,3,4 while also have them pointer towards the coresponding nodes

# current: 1 -> 2 -> 3 -> 4 -> 5 ->
# to be: 1 -> 4 -> 3 -> 2 -> 5 ->

# a variable to hold the current index as
# a previous_node variable -> holds the previous node as we need its pointer
# current_node_variable
# we need a dummy node at the begginging and have previous point to that, initially

# previous iterates untill it reaches the first node
# current is set to the next node
# then we need another loop for the indexes that we are going to reverse
# we create another variable called to_move
# have head point to whateve the dummy node points to


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index: int, end_index: int) -> None:
        if not self.head or start_index == end_index:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # 1. Reach the node just before the start_index
        for _ in range(start_index):
            prev = prev.next

        # 2. Set 'current' to the first node of the sub-list to be reversed
        current = prev.next

        # 3. Perform the reversal
        for _ in range(end_index - start_index):
            temp = current.next  # The node we want to move to the front
            current.next = (
                temp.next
            )  # 'current' jumps over 'temp' to point to the next one
            temp.next = prev.next  # 'temp' points to the current front of the sub-list
            prev.next = temp  # 'prev' now points to 'temp' as the new front

        self.head = dummy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1 -> 2 -> 3 -> 4 -> 5 -> None
    Reversed sublist (2, 4): 
    1 -> 2 -> 5 -> 4 -> 3 -> None
    Reversed entire linked list: 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed sublist of length 1 (3, 3): 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed empty linked list: 
    Empty -> None
    
"""
