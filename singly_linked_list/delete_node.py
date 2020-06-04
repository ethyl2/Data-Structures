"""
from code challenge session 06-04-2020 taught by Kapil Sharma

Given a node, delete it from its linked list.
No head is given.
Assume that the node is not the tail.
Return True if successful removal. False if not.

"""


class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None


def delete_node(my_node):
    if my_node == None or my_node.next == None:
        return False

    # Copy val from my_node.next and set my_node to have that value.
    # Set my_node.next to be my_node.next.next to jump over the old my_node.next (which isn't needed anymore)
    # Then return True

    # One way is to use a temp var:
    # next_node = my_node.next
    # my_node.value = next_node.value

    # Looks like the temp var isn't necessary.
    my_node.value = my_node.next.value
    my_node.next = my_node.next.next
    return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

print(delete_node(node2))
print(node1.next.value)
