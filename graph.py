class Graph:
    def __init__(self, edges, N):
        self.N = N
        self.matrix = [[0 for _ in range(N)] for _ in range(N)]
        for src, dst in edges:
            self.matrix[src][dst] = 1

    def __str__(self):
        str = ""
        for i in range(self.N):
            line = ""
            for j in self.matrix[i]:
                line += "{} ".format(j)
            str += "{}\n".format(line)
        return str

    def DFS(self):
        visited = [0 for i in range(self.N)]
        stack = []
        stack.append(0)
        while stack:
            node = stack.pop()
            print(node)
            visited[node] = 1
            for i in range(self.N):
                if self.matrix[node][i] and not visited[i]:
                    stack.append(i)

    def BFS(self):
        visited = [0 for _ in range(self.N)]
        queue = []
        queue.append(0)
        while queue:
            node = queue.pop(0)
            print(node)
            visited[node] = 1
            for dst in range(self.N):
                if self.matrix[node][dst] and not visited[dst]:
                    queue.append(dst)

edges = [(0, 1),(1, 3),(1, 2),(1, 5),
           (2, 4),(4, 5)]
N = 6
graph = Graph(edges, N)
print(graph)
graph.DFS()
print()
graph.BFS()