# Prim's algorithm for MST
Prim's algorithm has been used for finding the Minimum Spanning Tree (MST) from a Graph. In this implementation the input Graph is represented as **Adjacency Matrix**. Hence the complexity is **O(V^2)**, where V is the number of Vertices of the Graph.

The performance could be better if we use Adjacency List. The complexity then reduced to **O(ElogV)** using Binary Heap. E is the number of edges of the input Graph.  

## Input / Output Description 👹

The first line of each test case contains the number of vertices N (1 ≤ N ≤ 750). The vertices are labeled from 1 to N. The next N lines give the x and y coordinates of the vertices. These coordinates are integers with absolute values. After that there is a line containing the number of existing edges M (0 ≤ M ≤ 1000) followed by M lines describing the existing connections. Each edge is represented by two integers: the vertex numbers which are directly connected by the edge. the existing edge connections must not be altered.

For each set of input, output is a single line contains the total length of the new edges rounded to two decimal places.
