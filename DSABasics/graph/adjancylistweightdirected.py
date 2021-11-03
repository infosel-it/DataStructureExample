# A class to store a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


# A class to store adjacency list nodes
class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, edges, N):

        # A list of lists to represent an adjacency list
        self.adj = [None] * N

        # allocate memory for the adjacency list
        for i in range(N):
            self.adj[i] = []

        # add edges to the undirected graph
        for e in edges:
            # allocate node in adjacency list from src to dest
            node = Node(e.dest, e.weight)
            self.adj[e.src].append(node)


# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adj)):
        # print current vertex and all its neighboring vertices
        for edge in graph.adj[src]:
            print(f"({src} —> {edge.value}, {edge.weight}) ", end='')
        print()


if __name__ == '__main__':

    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge `(x, y, w)` represents an edge from `x` to `y` having weight `w`
    edges = [Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5), Edge(2, 1, 4),
            Edge(3, 2, 10), Edge(4, 5, 1), Edge(5, 4, 3)]

    # Input: No of vertices
    N = 6

    # construct a graph from a given list of edges
    graph = Graph(edges, N)

    # print adjacency list representation of the graph
    printGraph(graph)
