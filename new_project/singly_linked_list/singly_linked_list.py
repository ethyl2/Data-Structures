"""
From Artem's lecture 6/16/2020
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

    def __str__(self):
        if self.head is None:
            return('Empty SinglyLinkedList')
        curr = self.head
        output_string = f'Head: {str(self.head.value)} | '
        while curr:
            output_string += f'{str(curr.value)} -> '
            curr = curr.next_node
        output_string += f'None | Tail: {str(self.tail.value)}'
        return output_string

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        curr = self.head
        while curr:
            max_value = max(max_value, curr.value)
            curr = curr.next_node

        return max_value

    # remove the tail and return its value
    def remove_tail(self):
        # Edge case of empty sll
        if self.head is None:
            return None

        # If list only has one element, set head and tail to None
        if self.head == self.tail:
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value

        # Otherwise, traverse the sll until you get to the tail
        prev = self.head
        curr = self.head.next_node
        while curr.next_node:
            prev = curr
            curr = curr.next_node
        tail_value = curr.value

        # Detach the tail
        prev.next_node = None
        # Reassign the tail
        self.tail = prev

        return tail_value
