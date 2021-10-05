from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        que = deque()
        n = len(grid)
        minpath = float('inf')
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        que.append((0, 0, 1))
        visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
        visited[0][0] = True
        while que:
            r, c, m = que.popleft()
            if r == len(grid) - 1 and c == len(grid) - 1:
                minpath = min(minpath, m)
            for adj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                newr, newc = r + adj[0], c + adj[1]
                if 0 <= newr < len(grid) and 0 <= newc < len(grid) and not visited[newr][newc] and not grid[newr][
                                                                                                           newc] == 1:
                    visited[newr][newc] = True
                    que.append((newr, newc, m + 1))
        return -1 if minpath == float('inf') else minpath

