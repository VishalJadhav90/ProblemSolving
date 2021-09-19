from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited[r][c] = True
                    que.append((r, c, 0))

        l = 0
        while que:
            r, c, l = que.popleft()
            for pos in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                newr, newc = r + pos[0], c + pos[1]
                if newr < 0 or rows <= newr or newc < 0 or cols <= newc or grid[newr][newc] == 0 or visited[newr][newc]:
                    continue
                grid[newr][newc] = 2
                visited[newr][newc] = True
                que.append((newr, newc, l + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return l
