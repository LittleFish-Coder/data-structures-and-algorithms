# Tree

Number of nodes in a perfect binary tree

- Level 0: $2^0 = 1$ node
- Level 1: $2^1 = 2$ nodes
- Level 2: $2^2 = 4$ nodes
- Level 3: $2^3 = 8$ nodes
- Level h: $2^h$ nodes

Total number of nodes in a perfect binary tree with height h:

$2^0 + 2^1 + 2^2 + ... + 2^h = 2^{h+1} - 1$

## Binary Search Tree

Divide and conquer to do the `search`, `insert` and `delete` operations.

| Operation | Average | Worst |
| --- | --- | --- |
| Search | $O(log n)$ | $O(n)$ |
| Insert | $O(log n)$ | $O(n)$ |
| Delete | $O(log n)$ | $O(n)$ |

## Traverse
- In-order: left → root → right
- Pre-order: root → left → right
- Post-order: left → right → root

## Binary Heap
| Operation | Big-O|
| --- | --- |
| Search | $O(n)$ |
| Insert | $O(log n)$ |
| Delete | $O(log n)$ |