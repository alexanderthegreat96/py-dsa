# regular linked list
# but with a prev and not just a next
# which means, this will be pointing backwards

from typing import Optional


class Node:
    def __init__(self, value: any, key: any = None):
        self.key: any = key
        self.value: any = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value: any):
        new_node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length: int = 1

    def append(self, value: any) -> None:
        new_node: Node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        # previous tail node
        # also known as the current tail
        # before reassignment
        prev_tail_node = self.tail
        prev_tail_node.next = new_node

        # new node will become the tail
        # so it doesnt need to point to anything
        new_node.next = None

        # we are setting the previous pointer of the new node
        # to point to the previous tail
        new_node.prev = prev_tail_node

        # set the new tail
        # and increase the length
        self.tail = new_node
        self.length += 1

    def prepend(self, value: any) -> None:
        new_node: Node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        # grab the current head
        prev_head_node = self.head

        # new node must point to the previous
        # head node which is now a regular node
        new_node.next = prev_head_node

        # new node will not point to anything backwards
        # as it becomes the head
        new_node.prev = None

        # the previous head, now a regular node
        # will point backwards to the newly added node
        # which is now the new head
        prev_head_node.prev = new_node

        # set the head
        self.head = new_node
        self.length += 1

    def insert_before(self, node: Node, value: any) -> None:
        if self.length == 1:
            return self.prepend(value)

        new_node: Node = Node(value)

        # grab what the node we were adding stuff before
        # was pointing to
        prev_node_ptr: Node = node.prev

        # ensure the node points forwards
        # to the new node
        prev_node_ptr.next = new_node

        # new node must point towards the current node
        new_node.next = node

        # the new node must point backwards to the node
        # the current pointer was pointing towards
        new_node.prev = prev_node_ptr

        # ensure the current node points backwards to the new node
        node.prev = new_node
        self.length += 1

    def insert_after(self, node: Node, value: any) -> None:
        if self.length == 0:
            return self.append(value)

        new_node: Node = Node(value)

        # the node after the node we're adding stuff after
        next_node_ptr = node.next

        # we set the current node to point to the new node
        node.next = new_node

        # we set the new node to point backwards to the node
        # we're inserting after
        new_node.prev = node

        # we're setting the next pointer of the new node
        # to point to whatever node the node we're adding stuff
        # after pointed at
        new_node.next = next_node_ptr

        # ensure that the node after the new node
        # points backwards towards out new node
        next_node_ptr.prev = new_node
        self.length += 1

    def get(self, value: any) -> Optional[Node]:
        if self.length == 0:
            return None

        if self.length == 1:
            return self.head if self.head.value == value else None

        nodes = self.head
        while nodes:
            if nodes.value == value:
                return nodes
            nodes = nodes.next

    def remove(self, node: Node) -> None:
        if self.length == 0:
            return None

        # node that the node we want to remove was pointing to
        prev_node_ptr = node.prev
        next_node_ptr = node.next

        # the node must point to what the removed node is pointing to
        prev_node_ptr.next = node.next

        # ensure that the next node after this, points backwards
        # towards the node this removed pointer was pointing to
        next_node_ptr.prev = prev_node_ptr

        # unlink current node pointers
        node.next = None
        node.prev = None
        self.length -= 1

    # experimental method of removing a node by value
    # this is a time complexity of o of N and this should not be used
    # as it requires iteration
    # the entire point of a double linked list is to solve the iteration
    # problem a linked list has
    def pop(self, value: any) -> None:
        if self.length == 0:
            return

        # start looping
        current = self.head
        while current:
            # if found
            if current.value == value:
                is_head: bool = current == self.head
                is_tail: bool = current == self.tail

                # node before current
                node_before_current = current.prev
                # node after current
                node_after_current = current.next

                if is_head:
                    # reassign the new head
                    self.head = node_after_current
                    if self.head:
                        self.head.prev = None
                if is_tail:
                    # reassign the tail
                    self.tail = node_before_current
                    if self.tail:
                        self.tail.next = None

                if not is_head and not is_tail:
                    # node before current's next pointer is set to
                    # what current points to
                    node_before_current.next = current.next
                    # node after current's prev pointer is set to
                    # node before current
                    node_after_current.prev = node_before_current

                # unlink the pointers
                # for the node we want to remove
                current.next = None
                current.prev = None
                self.length -= 1
                break

            current = current.next

    def reverse(self) -> None:
        if self.length < 2:
            return

        # in a regular linked list we would normally
        # have to traverse untill we reach the tail
        # luckily, for a doubly linked list
        # the tail points backwards

        prev_node: Node = None
        current = self.head

        while current and current is not None:
            # set the prev node to the node
            # current was pointing backwards
            prev_node = current.prev

            # set current's backwards pointer
            # to current's next pointer
            # reversing basically
            current.prev = current.next

            # set current's next pointer towards the prev node
            current.next = prev_node

            # we're essentially using prev
            # to walk backwards by walking forwards
            # if that makes sense
            current = current.prev

        if prev_node is not None:
            self.tail = self.head
            self.head = prev_node.prev

    def print_list(self):
        nodes = self.head
        while nodes is not None:
            previous_node_value: Optional[any] = (
                nodes.prev.value if nodes.prev else "None"
            )
            current_node_value: any = nodes.value
            next_node_value: Optional[any] = nodes.next.value if nodes.next else "None"

            node_type: str = "[NODE]: "
            if not nodes.prev:
                node_type = "[HEAD]: "

            if not nodes.next:
                node_type = "[TAIL]: "

            print(
                f"{node_type}Prev Node Value: {previous_node_value} | Current Node Node: {current_node_value} | Next Node Value: {next_node_value}"
            )

            # move the pointer
            nodes = nodes.next


test = DoublyLinkedList(10)
test.append(20)
test.append(30)
test.append("alex")
test.append(60)
test.prepend(5)

alex_node = test.get("alex")
test.insert_after(alex_node, 150)

twenty_node = test.get(20)

test.insert_before(twenty_node, 600)
test.append(1000)

test.remove(twenty_node)
test.pop(30)
test.reverse()
test.reverse()
test.print_list()
