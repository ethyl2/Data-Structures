"""
https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm

Solve in O(n) time using O(1) additional space

given sll of integers l and int k, remove all els from l that have value == k
Return l

"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def remove_from_list(l, k):
    # Deal with edge cases first
    if l == None:
        return l

    # This deals with an example like l=[1000, 1000], k = 1000, so should return []
    while l.value == k:
        if l.next:
            l = l.next
        else:
            l = None
            return l

    # Loop through until the curr.next is k or there is no curr.next
    curr = l

    prev = None

    while curr.next:
        # print("Current: " + str(curr.value))
        # If we land on a k, unattach it by reassigning its prev's next to be its next
        if curr.value == k:
            prev.next = curr.next
            curr = curr.next
        # If the next value is a k, and there is still enough nodes for curr.next.next,
        # assign the curr's next to be its next.next to skip the next node (which contains k).
        elif curr.next.value == k and curr.next.next:
            prev = curr
            curr.next = curr.next.next
            curr = curr.next
            print(curr.value)
        # If the next node's value is k, but there aren't enough nodes to get the next.next,
        # the next node must be the tail. Set the curr's next to be none to deattach the tail.
        elif curr.next.value == k:
            curr.next = None
            curr = None
            # print("tail has value k")
            return l
        # Otherwise, continue along the sll
        else:
            prev = curr
            curr = curr.next
    # Last check to see if the tail's value is k. If so, detach it from the prev node.
    # This is important when a jump using next.next lands us on the tail.
    if curr.value == k:
        prev.next = None
    return l


node3 = ListNode(3)
node1 = ListNode(1)
node2 = ListNode(2)
node3_again = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node3.next = node1
node1.next = node2
node2.next = node3_again
node3_again.next = node4
node4.next = node5

# [3,1,2,3,4,5] -> [1,2,4,5]
print(remove_from_list(node3, 3).value)
# looks like it is getting the tail b/c adding a next. in here results in a nonetype error
print(remove_from_list(node1, 5).next.next.value)
