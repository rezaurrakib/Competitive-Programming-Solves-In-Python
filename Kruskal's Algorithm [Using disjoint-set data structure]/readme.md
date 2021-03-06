# Kruskal's Algorithm

It's follows a **Greedy approach** because at each step it adds to the forest an edge of least possible weight. This approach uses a disjoint-set data structure to maintain several disjoint sets of elements. Each set contains the vertices in a tree of the current forest. The operation **FIND-PARENT(U)** returns a representative element from the set that contains Vertex **U**. Thus, we can determine whether two vertices **U** and **V** belong to the same tree by testing whether **FIND-PARENT(U)** equals **FIND-PARENT(V)**. The combining of trees is accomplished by the UNION procedure. 

Kruskal's algorithm can be shown to run in **_O(E log V)_** time, where E is the number of edges in the graph and V is the number of vertices.
