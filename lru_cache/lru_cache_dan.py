from doubly_linked_list_lecture import DoublyLinkedList
# import sys
# sys.append('../doubly_linked_list')


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.order = DoublyLinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def report(self):
        values = []
        current_node = self.order.head
        while current_node.value:
            values.append(current_node.value)
            if current_node.next:
                current_node = current_node.next
            else:
                break
        print(str(values))
        print("My DLL's head: " + str(self.order.head.value))
        if self.order.head.next:
            print("My DLL's head.next: " + str(self.order.head.next.value))
        else:
            print("No head.next")
        print("My DLL's tail: " + str(self.order.tail.value))
        print("My DLL's length: " + str(self.order.length) + "\n")

    def modified_set(self, key, value):
        value_combo = (key, value)
        if key in self.storage:
            node = self.storage[key]
            # overwrite the old value
            node.value = value_combo
            # move this node to the tail
            self.order.move_to_end(node)
            return
        if len(self.storage) == self.limit:
            node = self.order.head
            self.order.delete(node)
            del self.storage[node.value[0]]
        self.order.add_to_tail(value_combo)
        self.storage[key] = self.order.tail

    def set(self, key, value):
        # I'm going to rename your 'value' variable to be 'value_combo' to keep things straight.
        value_combo = (key, value)
        # So, ignore the line below now.
        # value = (key, value)
        if key in self.storage:
            # Here, you need to update the value of the node, not what the dictionary is holding.
            # The value that the dictionary holds is the node, and it will be updated as soon as you update the node.
            # So, instead of what you have on line 59, we'll update the node on line 60.
            # self.storage[key] = value
            node = self.storage[key]
            node.value = value_combo
            # Now, you already have the node, so you don't need to loop through to find it.
            '''
            node = self.order.head
            while node:
                if node.value == value:
                    self.order.move_to_tail(node)
                    return
                else:
                    node = node.next
            '''
            # Just move it to the tail and return
            self.order.move_to_end(node)
            return
        if len(self.storage) == self.limit:
            node = self.order.head
            self.order.delete(node)
            del self.storage[node.value[0]]
        self.order.add_to_tail(value_combo)
        # Okay, so here you don't want to set the value of the key-value pair to be the tuple.
        # So, no self.storage[key] = value_combo
        # You need it to be the node, which is conveniently the tail.
        self.storage[key] = self.order.tail

    def get(self, key):
        if key not in self.storage:
            return None
        # On the next line of code, your 'value' variable is the node,
        # so you don't have to loop through the DLL list to find it.
        # You can move it to the end right away.
        value = self.storage[key]
        self.order.move_to_end(value)
        '''
        node = self.order.head
        while node:
            if node.value == value:
                self.order.move_to_end(node)
                break
            node = node.next
        '''
        # So we need to access 'value' (AKA the node)'s value[1] to get the actual value to return. So many values! :-)
        return value.value[1]


'''
cache = LRUCache(3)
cache.set('item2', 'b')
cache.report()
cache.set('item3', 'c')
cache.report()
cache.set('item1', 'a')
cache.report()
cache.set('item2', 'z')
cache.report()
print("a ==", cache.get('item1'))
'''

'''
cache = LRUCache(3)
cache.set('item1', 'a')
cache.report()
cache.set('item2', 'b')
cache.report()
cache.set('item3', 'c')
cache.report()
cache.set('item2', 'z')
cache.report()
print("a ==", cache.get('item1'))
'''
