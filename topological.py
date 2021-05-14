# A class to represent a graph object
class Graph:
    def __init__(self, edges, N):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            # add an edge from source to destination
            self.adjList[src].append(dest)


# Perform DFS on the graph and set the departure time of all
# vertices of the graph
def DFS(graph, v, discovered, departure, time):
    # mark the current node as discovered
    discovered[v] = True

    # set the arrival time of vertex `v`
    time = time + 1

    for u in graph.adjList[v]:
        # if `u` is not yet discovered
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)

    # ready to backtrack
    # set departure time of vertex `v`
    departure[time] = v
    time = time + 1
    print("departure....{}".format(departure))
    return time


# Function to perform a topological sort on a given DAG
def doTopologicalSort(graph, N):
    # `departure` stores the vertex number using departure time as an index
    departure = [-1] * 2 * N

    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
    time = 0

    # perform DFS on all undiscovered vertices
    for i in range(N):
        if not discovered[i]:
            print("discoverting {}".format(i))
            time = DFS(graph, i, discovered, departure, time)

    # Print the vertices in order of their decreasing
    # departure time in DFS, i.e., in topological order
    for i in reversed(range(2 * N)):
        if departure[i] != -1:
            print(departure[i])


if __name__ == '__main__':
    # List of graph edges as per the above diagram
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]

    # total number of nodes in the graph
    N = 8

    # build a graph from the given edges
    graph = Graph(edges, N)

    # perform topological sort
    doTopologicalSort(graph, N)
