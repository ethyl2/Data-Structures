# from dll_stack import Stack
from dll_queue import Queue
'''
import sys
sys.path.append('../queue_and_stack')
'''


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        while self:
            if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                    return
                else:
                    self = self.left
            else:
                if not self.right:
                    self.right = BinarySearchTree(value)
                    return
                else:
                    self = self.right

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        while self:
            if target is self.value:
                return True
            elif target < self.value:
                if not self.left:
                    return False
                else:
                    self = self.left
            else:
                if not self.right:
                    return False
                else:
                    self = self.right

    # Return the maximum value found in the tree

    def get_max(self):
        # Initially set the max value to be self.
        max = self.value
        while self.right:
            if self.right.value > max:
                max = self.right.value
            self = self.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left:
            self.left.for_each(cb)
        elif self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # AKA Inorder Traversal
    # Recursively:
    #   1. Visit left subtree
    #   2. Visit node
    #   3. Visit right subtree

    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        q = Queue()
        while node is not None:
            print(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            if q.len() > 0:
                node = q.dequeue()
            else:
                break
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


'''
my_bst = BinarySearchTree(1)
my_bst.insert(8)
my_bst.insert(5)
my_bst.insert(7)
my_bst.insert(6)
my_bst.insert(3)
my_bst.insert(4)
my_bst.insert(2)
my_bst.bft_print(my_bst)
'''
