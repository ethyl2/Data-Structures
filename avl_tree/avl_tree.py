"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """

    def update_height(self):
        # Find the largest distance between the head (node) and its subtree bottom
        pass

    """
    Updates the balance factor on the AVLTree class
    """

    def update_balance(self):
        # self.balance = height of left subtree - height of right subtree
        pass

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """

    def left_rotate(self):
        pass

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """

    def right_rotate(self):
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """

    def rebalance(self):
        pass

    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """

    def insert(self, key):
        new_node = Node(key)
        if self.node is None:
            self.node = new_node
        current_node = self.node
        while current_node:
            if key < current_node.key:
                if not current_node.left:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
        # Now, need to check if we need to rebalance.
