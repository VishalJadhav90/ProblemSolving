from collections import deque

class Solution:
    def shortestPath(self, A, edges, S):
        weight = [float('inf') for _ in range(A+1)]
        adj = [[float('inf') for _ in range(A+1)] for _ in range(A+1)]
        for i in range(1, A+1):
            adj[i][i] = 0

        for edge in edges:
            u, v, w = edge
            adj[u][v] = w

        weight[S] = 0
        # for v in range(A):
        #     weight[v] = adj[S][v]

        print("weight", weight, "from", S)

        que = deque()
        que.append(S)
        visited = [False for _ in range(A+1)]
        visited[S] = True
        while que:
            u = que.popleft()
            print("u", u)
            for v in range(1, A+1):
                if v == u: continue
                if adj[u][v] != float('inf'):
                    weight[v] = min(weight[v], weight[u]+adj[u][v])
                    que.append(v)
            print("weight", weight)

sol = Solution()
A = 5
edges = [
    [1, 2, 2],
    [1, 3, 4],
    [1, 4, 1],
    [4, 3, 2],
    [3, 5, 2],
    [5, 4, 4]
]
sol.shortestPath(A, edges, 1)
