"""
https://app.codesignal.com/interview-practice/task/RvDFbsNC3Xn7pnQfH/description

Given 2 huge ints represented by ll.
Ea ll el is a num from 0-9999 that represents a num with exactly 4 digits.
The represented num might have leading zeros.
Add up the huge ints and return result in same format.

a = 9876 -> 5432 -> 1999
b = 1 -> 8001

return 9876 -> 5434 -> 0
b/c
987654321999 + 18001 = 987654340000

Another example:
a = 123 -> 4 -> 5
b = 100 -> 100 -> 100

return 223 -> 104 -> 105
b/c
12300040005 + 10001000100 = 22301040105

# At least I can assume the ints are positive, so converting to strings is easier (than when dealing with neg nums)

"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

# Make a function that takes an int and returns a string with 4 digits
# Use it for each value in a to make the addend1
# Use it for each value in b to make the addend2
# Convert those strings into ints and add them to get the sum.
# Convert the sum into a string
# Break the string into 4-digit chunks and put each into a sll.


def addTwoHugeNumbers(a, b):
    # Edge case:
    # If either list has a single node and the value is zero, just return the other list
    if a.next == None and a.value == 0:
        return b
    if b.next == None and b.value == 0:
        return a

    # Convert the slls into ints and add them
    addend1 = sll_str_converter(a)
    addend2 = sll_str_converter(b)
    total = int(addend1) + int(addend2)

    # Break the total into chunks, 4 digits long, moving from right to left
    chunks = []
    str_total = str(total)
    print(str_total)

    for i in range(len(str_total), 0, -4):
        print("Current index: " + str(i))
        if i > 3:
            print(str_total[i-4:i])
            chunks.insert(0, str_total[i-4:i])
        else:
            # Get the last chunk, which might not be 4 digits long.
            print(str_total[0:i])
            chunks.insert(0, str_total[0:i])
    if chunks[0] == '':
        chunks.remove('')
    print(chunks)

    # Put the chunks into a new sll
    new_head = ListNode(int(chunks[0]))
    curr = new_head
    for i in range(1, len(chunks)):
        new_node = ListNode(int(chunks[i]))
        curr.next = new_node
        curr = new_node
    return new_head


def int_str_converter(num):
    num_to_string = str(num)
    num_zeros_needed = 4 - len(num_to_string)
    num_to_string = "0" * num_zeros_needed + num_to_string
    # print(num_to_string)
    return(num_to_string)


def sll_str_converter(sll):
    curr = sll
    output_string = ''
    while curr.next:
        output_string += int_str_converter(curr.value)
        curr = curr.next
    output_string += int_str_converter(curr.value)
    return output_string


# int_str_converter(41)

node1 = ListNode(9876)
node2 = ListNode(5432)
node1.next = node2

node3 = ListNode(1999)
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(8001)
node4.next = node5

# print(addTwoHugeNumbers(node1, node4).next.next.value)


node6 = ListNode(123)
node7 = ListNode(4)
node8 = ListNode(5)
node6.next = node7
node7.next = node8

node9 = ListNode(100)
node10 = ListNode(100)
node11 = ListNode(100)
node9.next = node10
node10.next = node11

# Expected output: 223 -> 104 -> 105
result = addTwoHugeNumbers(node6, node9)
curr = result
while curr:
    print(curr.value)
    curr = curr.next
