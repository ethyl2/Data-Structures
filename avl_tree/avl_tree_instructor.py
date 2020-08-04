outputdebug = False


def debug(msg):
    if outputdebug:
        print(msg)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.key, self.left, self.right}"


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        self.height = -1
        self.balance = 0

    def __repr__(self):
        return f"{self.node, self.height, self.balance}"

    def height(self):
        return self.node.height if self.node else 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        tree = self.node
        new_node = Node(key)

        if not tree:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    """
    Rebalance a particular (sub)tree
    """

    def rebalance(self):
        # key inserted. Let's check if we're balanced
        self.update_height()
        self.update_balance()

        while self.balance < -1 or self.balance > 1:
            # left subtree is heavier than the right side
            if self.balance > 1:
                # the left subtree's right subtree is heavier than its left side
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()

                self.right_rotate()
                self.update_height()
                self.update_balance()

            # right subtree is heavier than its left side
            if self.balance < -1:
                # the right subtree's left subtree is heavier than its right side
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()

                self.left_rotate()
                self.update_height()
                self.update_balance()

    """
    Perform a left rotation such that the right subtree becomes
    the parent of the current node. The current node should 
    become the new parent's left subtree
    """

    def right_rotate(self):
        # debug ('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = A.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    """
    Perform a right rotation such that the left subtree becomes
    the parent of the current node. The current node should 
    become the new parent's right subtree
    """

    def left_rotate(self):
        # debug ('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = A.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_height(self):
        if self.node != None:
            if self.node.left != None:
                self.node.left.update_height()
            if self.node.right != None:
                self.node.right.update_height()
            self.height = max(
                self.node.left.height if self.node.left else -1,
                self.node.right.height if self.node.right else -1
            ) + 1
        else:
            self.height = -1

    def update_balance(self, recurse=True):
        if self.node != None:
            if self.node.left != None:
                self.node.left.update_balance()
            if self.node.right != None:
                self.node.right.update_balance()

            self.balance = (self.node.left.height if self.node.left else 0) - \
                (self.node.right.height if self.node.right else 0)
        else:
            self.balance = 0

    # def check_balanced(self):
    #     if self == None or self.node == None:
    #         return True

    #     # We always need to make sure we are balanced
    #     self.update_heights()
    #     self.update_balances()
    #     return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        '''
        self.update_height()  # Must update heights before balances
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')


# Usage example
if __name__ == "__main__":
    a = AVLTree()
    print("----- Inserting -------")
    #inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist:
        a.insert(i)

    a.display()

    # print ("----- Deleting -------")
    # a.delete(3)
    # a.delete(4)
    # # a.delete(5)
    # a.display()

    # print ()
    # print ("Input            :", inlist )
    # print ("deleting ...       ", 3)
    # print ("deleting ...       ", 4)
    # print ("Inorder traversal:", a.inorder_traverse())
