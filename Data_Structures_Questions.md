Answer the following questions for each of the data structures you implemented as part of this project.

| method    |    Array     |           DLL |
| --------- | :----------: | ------------: |
| append    |      1       |             1 |
| print nth |      1       |             n |
| add front |      n       |             1 |
| del front |      n       |             1 |
| del mid   |      n       | 1 (n to find) |
| find      | n (or log n) |             n |

## Queue

1. What is the runtime complexity of `enqueue`?

   O(1) because a linked list does not require a contiguous block of memory.

2. What is the runtime complexity of `dequeue`?

   O(1) because a linked list does not require a contiguous block of memory.

3. What is the runtime complexity of `len`?

## Binary Search Tree

1. What is the runtime complexity of `insert`? O(n) because in worst case, need to touch each node.

Example: inserting 1 in 7 -> 2

https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/

2. What is the runtime complexity of `contains`? O(log n)

3. What is the runtime complexity of `get_max`? O(n) because in worst case, need to touch each node (??)

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(1)?

2. What is the runtime complexity of `ListNode.insert_before`? O(1)?

3. What is the runtime complexity of `ListNode.delete`? O(1)?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(1)?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(1)?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(1)?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(1)?

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(1) when the node is the parameter. O(n) to find if the value is the parameter, so the node has to be found first.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better? DLL's delete worst-case is O(1) when the node is the parameter, while the worst case runtime of Array.splice would be O(n) -> such as when the first item is deleted, with no addition of another item, all the other items must be shifted up an index.

    About array.splice:

    array.splice(index, howManyToRemove, item1toAdd, ....., itemXtoAdd)

    The array.splice() method adds/removes items to/from an array, and returns the removed item(s).

    This method changes the original array.

## For reference:

- Dictionaries give us constant access time AKA O(1)
