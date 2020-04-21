class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def make_new_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.add(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def find_mid(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer


our_ll = LinkedList()
our_ll.make_new_head(5)
our_ll.make_new_head(4)
our_ll.make_new_head(3)
our_ll.make_new_head(2)
our_ll.make_new_head(1)

our_ll.print_list()

our_ll.reverse()

our_ll.print_list()
print('\n')
print(our_ll.find_mid().value)
print('\n')
our_ll.reverse()
our_ll.add_to_tail(6)
our_ll.print_list()
