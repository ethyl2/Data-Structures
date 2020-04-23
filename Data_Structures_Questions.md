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

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(n) to find

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

---

## For reference:

- Dictionaries give us constant access time AKA O(1)
