'''
Generic heap means that the user can define their own priority function and pass it to the heap to use.
If no comparator function is passed in to the heap constructor, it should default to being a max heap.
'''

# Here's non-lambda version of the default comparator


def is_higher_priority(x, y): return x > y


class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        # Adds the input value into the heap.
        # This method should ensure that the inserted value is in the correct spot in the heap.
        self.storage.append(value)
        current_index = len(self.storage) - 1

        while current_index >= 0:
            self._bubble_up(current_index)
            # Move to the parent
            current_index = (current_index - 1)//2

    def delete(self):
        # Removes and returns the 'topmost' value from the heap.
        # This method needs to ensure that the heap property is maintained
        # after the topmost element has been removed.
        topmost = self.storage.pop(0)
        current_index = 0
        while current_index <= len(self.storage) - 1:
            self._sift_down(current_index)
            current_index += 1
        return topmost

    def get_priority(self):
        # Returns the highest priority value in the heap in constant time.
        return self.storage[0]

    def get_size(self):
        # Returns the number of elements stored in the heap.
        return len(self.storage)

    def _bubble_up(self, index):
        # Moves the element at the specified index "up" the heap
        # by swapping it with its parent
        # if the parent's value has less priority than the value at the specified index.
        if index == 0:
            return
        parent_index = (index-1)//2

        current_value = self.storage[index]
        if self.comparator(self.storage[parent_index], self.storage[index]) == False:
            self.storage[index] = self.storage[parent_index]
            self.storage[parent_index] = current_value

    def _sift_down(self, index):
        # grabs the indices of this element's children
        # and determines which child has a value with higher priority.
        # If the winning child's value has higher priority than the parent's value,
        # the child element is swapped with the parent.
        left_index = (2*index + 1)
        right_index = (2*index + 2)
        max_priority_index = index
        parent_value = self.storage[index]
        if left_index <= len(self.storage) - 1 and self.comparator(self.storage[left_index], self.storage[max_priority_index]):
            max_priority_index = left_index
        if right_index <= len(self.storage) - 1 and self.comparator(self.storage[right_index], self.storage[max_priority_index]):
            max_priority_index = right_index
        if max_priority_index != index:
            self.storage[index] = self.storage[max_priority_index]
            self.storage[max_priority_index] = parent_value
        return


'''
my_heap = Heap()
my_heap.insert(5)
my_heap.insert(6)
my_heap._bubble_up(1)
print(my_heap.storage)
my_heap.insert(7)
my_heap._sift_down(0)
print(my_heap.storage)
'''
