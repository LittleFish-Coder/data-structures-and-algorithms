# Graph

There are many ways to represent a graph
- Edge List
- Adjacency Matrix
- Adjacency List

## Edge List
```
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]
```

## Adjacency Matrix
```
graph = [
  [0, 0, 1, 0],
  [0, 0, 1, 1],
  [1, 1, 0, 1],
  [0, 1, 1, 0]
]
```

## Adjacency List
```
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]
```

## Space Complexity by Representation
- Edge List: O(E)
- Adjacency Matrix: O(V^2)
- Adjacency List: O(V + E)