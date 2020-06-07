"""
https://app.codesignal.com/interview-practice/task/HmNvEkfFShPhREMn4

Try to solve in O(n) time, using O(1) additional space.

Given a head of a sll of ints, determine whether the sll is a palindrome.

0 -> 1 -> 0
True

1 -> 2 -> 2 -> 3
False
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def is_list_palindrome(l):
    # Navigate thru sll, storing the values in a data type to evaluate later -- string??
    # See if string is even,
    #   if so, does second half reversed == first half?
    #       if so, return True
    #       if not, return False
    # If string is odd, slice front half, leaving the middle value, and last half and do the same check as above.
    #

    # First, dealing with edge cases:
    if l == None:
        print("l is empty")
        return True
    if l.next == None:
        print("l is a single node")
        return True
    if type(l) != ListNode:
        print("l is not a ListNode")
        return True

    '''
    # Using a string only works with single digit ints
    my_string = str(abs(l.value))
    curr = l.next
    while curr.next:
        my_string += str(abs(curr.value))
        curr = curr.next
    my_string += str(abs(curr.value))
    # print(my_string)
    return is_palindrome(my_string)
    '''
    # Using a list instead
    my_list = [l.value]
    curr = l.next
    while curr.next:
        my_list.append(curr.value)
        curr = curr.next
    my_list.append(curr.value)

    return is_palindrome_list(my_list)


def is_palindrome_list(my_list):
    is_even = len(my_list) % 2 == 0
    if is_even:
        # print(my_list[:len(my_list)//2])
        # print(list(reversed(my_list[len(my_list)//2:])))
        return my_list[:len(my_list)//2] == list(reversed(my_list[len(my_list)//2:]))
    else:
        # print(my_list[:len(my_list)//2])
        # print(list(reversed(my_list[len(my_list)//2 + 1:])))
        return my_list[:len(my_list)//2] == list(reversed(my_list[len(my_list)//2 + 1:]))


def is_palindrome(my_string):
    is_even = len(my_string) % 2 == 0
    # print(is_even)
    if is_even:
        # print(my_string[: len(my_string)//2])
        # print(my_string[-1:len(my_string)//2 - 1:-1])
        return my_string[: len(my_string)//2] == my_string[-1:len(my_string)//2 - 1:-1]
    else:
        # print(my_string[: (len(my_string) - 1)//2])
        # print(my_string[-1:(len(my_string) - 1)//2:-1])
        return my_string[: (len(my_string) - 1)//2] == my_string[-1:(len(my_string) - 1)//2:-1]


node1 = ListNode(0)
node2 = ListNode(1)
node1.next = node2

node3 = ListNode(2)
node2.next = node3

node4 = ListNode(1)
node3.next = node4

# print(is_list_palindrome(node1))

node5 = ListNode(0)
node4.next = node5

print(is_list_palindrome(node1))
'''
test = [1, 3, 2, 2, 2]
print('testing palindrome function: ')
print(is_palindrome(test))
test2 = [1, 5, 2, 4]
print(is_palindrome(test2))
'''
