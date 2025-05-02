# Final Exam

## Question 1
Consider a directed graph G = (V,E) with non-negative edge lengths and two distinct vertices s and t of V. Let P denote a shortest path from s to t in G. If we add 10 to the length of every edge in the graph, then: [Check all that apply.]

- [] PP definitely does not remain a shortest s-ts−t path.
- [X] PP might or might not remain a shortest s-ts−t path (depending on the graph).
- [] PP definitely remains a shortest s-ts−t path.
- [X] If PP has only one edge, then PP definitely remains a shortest s-ts−t path.

## Question 2
What is the running time of depth-ﬁrst search, as a function of n and m, if the input graph G=(V,E) is represented by an adjacency matrix (i.e., NOT an adjacency list), where as usual n=|V| and m=|E|?

- [] $\theta(n^2\log m)$
- [] $\theta(n*m)$
- [] $\theta(n+m)$
- [X] $\theta(n^2)$

## Question 3

What is the asymptotic running time of the Insert and Extract-Min operations, respectively, for a heap with nn objects?

- [X] $\Theta(\log n)$ and $\Theta(\log n)$
- [] $\Theta(n)$ and $\Theta(1)$
- [] $\Theta(1)$ and $\Theta(\log n)$
- [] $\Theta(\log n)$ and $\Theta(1)$

## Question 4

On adding one extra edge to a directed graph G, the number of strongly connected components...?

- [X] ...might or might not remain the same (depending on the graph).
- [] ...cannot decrease
- [] ...cannot decrease by more than 1
- [] ...cannot change

## Question 5

Which of the following statements hold? (As usual n and m denote the number of vertices and edges, respectively, of a graph.)
[Check all that apply.]

- [X] Depth-first search can be used to compute a topological ordering of a directed acyclic graph in O(m+n) time.
- [X] Breadth-first search can be used to compute shortest paths in O(m+n) time (when every edge has unit length).
- [X] Breadth-first search can be used to compute the connected components of an undirected graph in O(m+n) time.
- [X] Depth-first search can be used to compute the strongly connected components of a directed graph in O(m+n) time.

## Question 6

When does a directed graph have a unique topological ordering?

- [X] None of the other options
- [] Whenever it has a unique cycle
- [] Whenever it is a complete directed graph
- [] Whenever it is directed acyclic

## Question 7

Suppose you implement the operations Insert and Extract-Min using a sorted array (from biggest to smallest).  What is the worst-case running time of Insert and Extract-Min, respectively? (Assume that you have a large enough array to accommodate the Insertions that you face.)

- [] $\Theta(n)$ and $\Theta(n)$
- [X] $\Theta(n)$ and $\Theta(1)$
- [] $\Theta(\log n)$ and $\Theta(1)$
- [] $\Theta(1)$ and $\Theta(n)$

## Question 8

Which of the following patterns in a computer program suggests that a heap data structure could provide a significant speed-up (check all that apply)?

- [X] Repeated minimum computations
- [X] Repeated maximum computations
- [] None of the other options
- [] Repeated lookups

## Question 9

Which of the following patterns in a computer program suggests that a hash table could provide a significant speed-up (check all that apply)?

- [] None of the other options
- [] Repeated maximum computations
- [] Repeated minimum computations
- [X] Repeated lookups

## Question 10

Which of the following statements about Dijkstra's shortest-path algorithm are true for input graphs that might have some negative edge lengths?  [Check all that apply.]

- [] It is guaranteed to correctly compute shortest-path distances (from a given source vertex to all other vertices).
- [X] It is guaranteed to terminate.
- [] It may or may not terminate (depending on the graph).
- [X] It may or may not correctly compute shortest-path distances (from a given source vertex to all other vertices), depending on the graph.


