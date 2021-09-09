from collections import deque


class Solution:
    def checkBlack(self, A, r, c, visited):
        que = deque()
        que.append((r, c))
        visited[r][c] = True
        while que:
            r, c = que.popleft()
            for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                newr = r + x
                newc = c + y
                if (0 <= newr < len(A)) and (0 <= newc < len(A[0])):
                    if (not visited[newr][newc]) and (A[newr][newc] == 'X'):
                        visited[newr][newc] = True
                        que.append((newr, newc))

    # @param A : list of strings
    # @return an integer
    def black(self, A):
        count = 0
        visited = [[False for _ in s] for s in A]
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 'O':
                    visited[r][c] = True
                    continue

                if A[r][c] == 'X' and (not visited[r][c]):
                    self.checkBlack(A, r, c, visited)
                    count += 1
                print("visited", visited)
        print("count", count)
        return count

sol = Solution()
A = ['OOOXOOO',
     'OOXXOXO',
     'OXOOOXO']
sol.black(A)