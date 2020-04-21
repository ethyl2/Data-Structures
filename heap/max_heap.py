class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # Adds the input value into the heap.
        # This method should ensure that the inserted value is in the correct spot in the heap.
        print("Time to add " + str(value))
        self.storage.append(value)
        # current_index = self.storage.index(value)
        current_index = len(self.storage) - 1
        print("Let's start by putting it at index " + str(current_index))
        # print(current_index)
        while current_index > 0:
            self._bubble_up(current_index)
            # self._sift_down(current_index)
            # current_index -= 1
            current_index = (current_index - 1)//2
        print("\n")

    def delete(self):
        # Removes and returns the 'topmost' value from the heap.
        # This method needs to ensure that the heap property is maintained after the topmost element has been removed.
        topmost = self.storage.pop(0)
        return topmost

    def get_max(self):
        # Returns the maximum value in the heap in constant time.
        return self.storage[0]

    def get_size(self):
        # Returns the number of elements stored in the heap.
        return len(self.storage)

    def _bubble_up(self, index):
        # Moves the element at the specified index "up" the heap
        # by swapping it with its parent if the parent's value is less than the value at the specified index.
        if index == 0:
            return
        parent_index = (index-1)//2
        # current_value = self.storage[len(self.storage)-1] # I accidentally wrote this.
        current_value = self.storage[index]
        if self.storage[parent_index] < self.storage[index]:
            print("time to bubble up because parent " +
                  str(self.storage[parent_index]) + " < " + str(self.storage[index]))
            self.storage[index] = self.storage[parent_index]
            self.storage[parent_index] = current_value
        else:
            print("no need to bubble up because parent " +
                  str(self.storage[parent_index]) + " >= " + str(self.storage[index]))

    def _sift_down(self, index):
        # grabs the indices of this element's children
        # and determines which child has a larger value.
        # If the larger child's value is larger than the parent's value,
        # the child element is swapped with the parent.
        left_index = (2*index + 1)
        right_index = (2*index + 2)
        max_index = index
        parent_value = self.storage[index]
        if self.storage[left_index] > self.storage[max_index]:
            max_index = left_index
        if self.storage[right_index] > self.storage[max_index]:
            max_index = right_index
        if max_index != index:
            self.storage[index] = self.storage[max_index]
            self.storage[max_index] = parent_value
        return


'''
my_heap = Heap()
my_heap.insert(19)

my_heap.insert(100)

my_heap.insert(36)

my_heap.insert(17)
my_heap.insert(3)
my_heap.insert(25)
my_heap.insert(1)
my_heap.insert(2)
my_heap.insert(7)
'''
# print(my_heap.get_max())
# print(my_heap.get_size())
# print(my_heap.storage)
# my_heap._sift_down(0)
# my_heap._bubble_up(1)
# print(my_heap.storage)
