# Case Study: Implementation of Stack and Queue Operations Using Linked Lists

## 1. Aim
To implement Stack and Queue data structures using linked lists and perform basic insertion, deletion, display, and peek operations.

## 2. Introduction
A linked list is a linear data structure made up of nodes. Each node contains data and a pointer (link) to the next node.

A linked list can grow or shrink dynamically according to the number of elements stored.

A Stack and a Queue are two important linear data structures that can be implemented using linked lists.

## 3. Stack Using Linked List
A Stack follows the **LIFO (Last In, First Out)** principle. The element inserted last is removed first.

### Stack Operations
- **Push:** Adds an element to the top of the stack.
- **Pop:** Removes the top element.
- **Peek:** Displays the top element without removing it.
- **Display:** Shows all stack elements from top to bottom.

### Example
If we push 10, 20, and 30 into a stack, its contents become:

`Top → 30 → 20 → 10 → NULL`

After performing Pop, 30 is removed:

`Top → 20 → 10 → NULL`

## 4. Queue Using Linked List
A Queue follows the **FIFO (First In, First Out)** principle. The element inserted first is removed first.

### Queue Operations
- **Enqueue:** Adds an element at the rear.
- **Dequeue:** Removes an element from the front.
- **Peek:** Displays the front element without removing it.
- **Display:** Shows all queue elements from front to rear.

### Example
After inserting 10, 20, and 30, the queue becomes:

`Front → 10 → 20 → 30 ← Rear`

After performing Dequeue, 10 is removed:

`Front → 20 → 30 ← Rear`

## 5. Algorithm

### Stack Algorithm
1. Create an empty stack with `top = NULL`.
2. For Push, create a new node and place it at the top.
3. For Pop, remove the top node and update the top pointer.
4. For Peek, display the top node's data.
5. Traverse the linked list to display all elements.

### Queue Algorithm
1. Create an empty queue with `front = NULL` and `rear = NULL`.
2. For Enqueue, create a node and attach it at the rear.
3. For Dequeue, remove the node at the front and update the front pointer.
4. If the queue becomes empty, set both front and rear to NULL.
5. Traverse from front to rear to display all elements.

## 6. Output

### Stack Output
```text
10 pushed into stack
20 pushed into stack
30 pushed into stack
Stack (top to bottom): 30 20 10
Top element: 30
Popped: 30
Stack (top to bottom): 20 10
```

### Queue Output
```text
10 added to queue
20 added to queue
30 added to queue
Queue (front to rear): 10 20 30
Front element: 10
Removed: 10
Queue (front to rear): 20 30
```

## 7. Time and Space Complexity

Let n be the number of elements in the stack or queue.

| Operation | Time Complexity |
|---|---|
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Stack Peek | O(1) |
| Stack Display | O(n) |
| Queue Enqueue | O(1) |
| Queue Dequeue | O(1) |
| Queue Peek | O(1) |
| Queue Display | O(n) |

**Space Complexity:** O(n) for both Stack and Queue, because each element is stored in a linked-list node.

## 8. Advantages
- The size can grow or shrink dynamically.
- No fixed array capacity is required.
- Insertion and deletion at the required ends are efficient.
- Memory is allocated as needed.

## 9. Limitations
- Each node requires extra memory for a link.
- Elements cannot be accessed directly by index.
- Traversal is required to visit elements in the list.
- Incorrect pointer handling may cause errors or memory leaks.

## 10. Applications
- **Stack:** Function calls, undo operations, expression evaluation, and browser history.
- **Queue:** Printer scheduling, task processing, customer service systems, and request handling.

## 11. Conclusion
Stack and Queue can both be implemented efficiently using linked lists. Stack follows LIFO and performs insertion and deletion at the top. Queue follows FIFO and performs insertion at the rear and deletion at the front. Both structures support dynamic memory usage and efficient basic operations.