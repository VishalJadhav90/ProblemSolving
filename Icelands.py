from collections import deque


class Solution:
    def recFlood(self, grid, r, c):
        if grid[r][c] == "0":
            return

        que = deque()
        grid[r][c] = "0"
        que.append((r, c))
        while que:
            rr, cc = que.popleft()
            for moves in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                newr, newc = rr + moves[0], cc + moves[1]
                if newr < 0 or newr >= len(grid) or newc < 0 or newc >= len(grid[0]) or grid[newr][newc] == "0":
                    continue
                grid[newr][newc] = "0"
                que.append((newr, newc))

    def numIslands(self, grid: List[List[str]]) -> int:
        iceland = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    iceland += 1
                    self.recFlood(grid, r, c)
        return iceland
