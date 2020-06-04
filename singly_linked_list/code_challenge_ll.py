class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverse_list(head):
    prev = None
    curr = head
    while curr is not None:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
    print(prev.value)
    return prev


def remove_val(head, val):
    if head.value == val:
        print("head is val")
        return head.next
    curr = head
    while curr.next and curr.next.value != val:
        curr = curr.next
    if curr.next and curr.next.value == val:
        curr.next = curr.next.next
    return head


def remove_kth_node(head, k):
    # Delete the kth from the end

    # Make sure that head is a ListNode
    if type(head) != ListNode:
        return head

    if k == 0:
        return head.next

    # Find out length of list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next

    # if k is past the length of list, just return the head
    if k > length:
        return head

    # Point current back to head
    current = head
    # Loop through list until k-1
    for i in range(k-1):
        current = current.next

    # Skip over kth el
    current.next = current.next.next
    return head


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
# print(node1.next.value)
node3 = ListNode(3)
node2.next = node3
# print(node2.next.value)
# print(node1.next.next.value)

# print(reverse_list(node1))
new_head = reverse_list(node1)
print(new_head.value)
# print(new_head.next.value)

new_head = reverse_list(node3)

altered_list = remove_val(node1, 1)
print(altered_list.value)

node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5

print(remove_kth_node(node2, 0).value)
print(remove_kth_node(node3, 2).next.value)
