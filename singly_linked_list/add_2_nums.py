"""
https://leetcode.com/problems/add-two-numbers/
Given: 2 non-empty sll (well, the heads of them), 
representing 2 non-neg ints, with the digits stored in reverse order.

Add the 2 nums and return it as a sll

(2 -> 4 -> 3) + ( 5 -> 6 -> 4)
342 + 465

return 7-> 0 -> 8
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_2_nums(self, l1, l2):
        val1 = ''
        current_node = l1
        while current_node:
            val1 = str(current_node.val) + val1
            current_node = current_node.next

        val2 = ''
        current_node = l2
        while current_node:
            val2 = str(current_node.val) + val2
            current_node = current_node.next

        result = int(val1) + int(val2)
        tail = ListNode(str(result)[0], None)
        current_node = tail
        for digit in str(result)[1:]:
            new_node = ListNode(digit, current_node)
            current_node = new_node

        return(current_node)

        '''
        # Same thing basically, but with more comments.
        # Convert l1 into a string
        num1 = ''
        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next
        
        # Convert l2 into a string
        num2 = ''
        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next

        # Convert them into ints and add them together
        total = int(num1) + int(num2)

        # Convert the result into a string
        total = str(total)

        # Convert the result into a sll
        curr = ListNode(total[0])
        for digit in total[1:]:
            new_node = ListNode(digit, curr)
            curr = new_node

        # Return the head of the sll
        return curr
        '''
