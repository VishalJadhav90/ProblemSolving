class Solution:
    def isPresent(self, board, word, visited, r, c, w):
        if r >= len(board) and c >= len(board[0]):
            return False
        if w == len(word):
            return True
        result = False
        for adj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r+adj[0], c+adj[1]
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and not visited[nr][nc] and board[nr][nc]==word[w]:
                visited[nr][nc] = True
                result = result or self.isPresent(board, word, visited, nr, nc, w+1)
                visited[nr][nc] = False
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = [[False for _ in range(cols)] for _ in range(rows)]
                    visited[r][c] = True
                    result = self.isPresent(board, word, visited, r, c, 1)
                    if result: return result
        return False
