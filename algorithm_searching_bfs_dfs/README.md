# Searching (Traversal)

## Time Complexity
| Algorithm | Time Complexity |
| --- | --- |
| Linear Search | $O(n)$ |
| Binary Search | $O(log n)$ |

## DFS vs BFS

Which one to use when searching for a path in a graph?

- **BFS:** Shortest path, minimum number of edges (More memory)
- **DFS:** find all possible paths (Less memory)

### Time and Space Complexity:
| Algorithm | Time Complexity | Space Complexity |
| --- | --- | --- |
| BFS | $O(V)$ | $O(V)$ |
| DFS | $O(V)$ | $O(h)$ |

\* h: height of the tree
> https://stackoverflow.com/q/9844193

## Tree Traversal
```
    9
   / \
  4   20
 / \  / \   
1  6 15 170
```

- **Breadth First Search (BFS):**
  - Level-order: 9, 4, 20, 1, 6, 15, 170

- **Depth First Search (DFS):**
  - In-order: 1, 4, 6, 9, 15, 20, 170
  - Pre-order: 9, 4, 1, 6, 20, 15, 170
  - Post-order: 1, 6, 4, 15, 170, 20, 9

- **Pre-order:** Root, Left, Right
- **In-order:** Left, Root, Right
- **Post-order:** Left, Right, Root
