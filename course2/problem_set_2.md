# Problem Set 2

## Question 1

Consider a directed graph with distinct and nonnegative edge lengths and a source vertex s. Fix a destination vertex t, and assume that the graph contains at least one s-t path.  Which of the following statements are true?  [Check all that apply.]

-[] The shortest s-t path must include the minimum-length edge of G.
	- FALSE: consider for example a graph with nodes v1, v2, v3 and weights (v1, v2) of length 1, (v2, v3) of length 2 and (v1, v3) of length 2.
-[] The shortest s-t path must exclude the maximum-length edge of G.
	- FALSE: consider for example a graph with 3 vertices, v1, v2, v3, and one path (v1, v3) with weight 2 and one path (v1 -> v2 -> v3) where each edge has weight 1.
-[X] There is a shortest s-t path with no repeated vertices (i.e., a "simple" or "loopless" such path).
	- TRUE
	- Since Dijkstra's algorithm puts each vertex into X only once, how could there be a repeated vertex in the path?
-[X] The shortest (i.e., minimum-length) s-t path might have as many as n−1 edges, where n is the number of vertices.
	- TRUE: consider for example a directed linear path.

## Question 2

Consider a directed graph G with a source vertex s, a destination t, and nonnegative edge lengths. Under what conditions is the shortest s-t path guaranteed to be unique? 

- When all edges lengths are distinct positive integers and the graph G contains no directed cycles.
  - FALSE
- When all edge lengths are distinct powers of 2.
  - TRUE
- When all edge lengths are distinct positive integers.
  - FALSE: consider a graph (v1, v2), (v1, v3), (v2, v4) and (v3, v4). The sum of the top edges equals the sum of the bottom edges with different numbers (e.g., 3 + 4 and 5 + 2).
- None of the other options are correct.
  - FALSE

## Question 3

Consider a directed graph G=(V,E) and a source vertex s with the following properties: edges that leave the source vertex s have arbitrary (possibly negative) lengths; all other edge lengths are nonnegative; and there are no edges from any other vertex to the source s. Does Dijkstra's shortest-path algorithm correctly compute shortest-path distances (from s) in this graph?
1 point

- Only if we add the assumption that G contains no directed cycles with negative total weight.
  - FALSE
- Never
  - FALSE
- Maybe, maybe not (depends on the graph)
  - FALSE
- Always
  - TRUE?

## Question 4

Consider a directed graph G and a source vertex s. Suppose G has some negative edge lengths but no negative cycles, meaning G does not have a directed cycle in which the sum of the edge lengths is negative. Suppose you run Dijkstra's algorithm on G (with source s).  Which of the following statements are true? [Check all that apply.]

-[X] Dijkstra's algorithm always terminates, but in some cases the paths it computes will not be the shortest paths from s to all other vertices.
-[X] Dijkstra's algorithm always terminates, and in some cases the paths it computes will be the correct shortest paths from s to all other vertices.
-[] Dijkstra's algorithm might loop forever.
-[] It's impossible to run Dijkstra's algorithm on a graph with negative edge lengths.

## Question 5

Consider a directed graph G and a source vertex s. Suppose G contains a negative cycle (a directed cycle in which the sum of the edge lengths is negative) and also a path from s to this cycle. Suppose you run Dijkstra's algorithm on G (with source s). Which of the following statements are true? [Check all that apply.]

-[X] Dijkstra's algorithm always terminates, but in some cases the paths it computes will not be the shortest paths from s to all other vertices.
-[] It's impossible to run Dijkstra's algorithm on a graph with a negative cycle.
-[] Dijkstra's algorithm always terminates, and in some cases the paths it computes will be the correct shortest paths from s to all other vertices.
-[] Dijkstra's algorithm might loop forever.
