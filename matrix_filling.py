from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque()
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    que.append((r, c))
                else:
                    mat[r][c] = -1

        while que:
            r, c = que.popleft()
            for pos in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr = r + pos[0]
                nc = c + pos[1]
                if nr < 0 or rows <= nr or nc < 0 or cols <= nc or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                que.append((nr, nc))
        return mat

