# Problem Set #3

## Question 1

Suppose you implement the functionality of a priority queue using a sorted array (e.g., from biggest to smallest). What is the worst-case running time of Insert and Extract-Min, respectively? (Assume that you have a large enough array to accommodate the Insertions that you face.)

- $\Theta(1)$ and $\Theta(n)$
- $\Theta(n)$ and $\Theta(n)$
- $\Theta(\log n)$ and $\Theta(1)$
- $\Theta(n)$ and $\Theta(1)$   **CORRECT**

## Question 2

Suppose you implement the functionality of a priority queue using an unsorted array. What is the worst-case running time of Insert and Extract-Min, respectively? (Assume that you have a large enough array to accommodate the Insertions that you face.)

- $\Theta(1)$ and $\Theta(\log n)$
- $\Theta(n)$ and $\Theta(1)$
- $\Theta(1)$ and $\Theta(n)$   **CORRECT**
- $\Theta(n)$ and $\Theta(n)$

## Question 3

You are given a heap with nn elements that supports Insert and Extract-Min. Which of the following tasks can you achieve in O(\log n) time?

- None of these.
- Find the median of the elements stored in the heap.
- Find the largest element stored in the heap.
- Find the fifth-smallest element stored in the heap.   **CORRECT**

## Question 4

You are given a binary tree (via a pointer to its root) with nn nodes. As in lecture, let size(x) denote the number of nodes in the subtree rooted at the node x. How much time is necessary and sufficient to compute size(x) for every node x of the tree?

- $\Theta(n^2)$
- $\Theta(n)$  **CORRECT**
- $\Theta(height)$
- $\Theta(n \log n)$

Hint: How many distinct quantities are you responsible for computing?

## Question 5

Suppose we relax the third invariant of red-black trees to the property that there are no three reds in a row. That is, if a node and its parent are both red, then both of its children must be black. Call these relaxed red-black trees. Which of the following statements is not true?

- The height of every relaxed red-black tree with n nodes is O(\log n)
- Every binary search tree can be turned into a relaxed red-black tree (via some coloring of the nodes as black or red).
- Every red-black tree is also a relaxed red-black tree. **INCORRECT**
    - The third invariant is only easier to satisfy, and the other three invariants are the same.
- There is a relaxed red-black tree that is not also a red-black tree. **INCORRECT**
    - E.g., a chain of three nodes, with the root colored black and the other two nodes colored red.