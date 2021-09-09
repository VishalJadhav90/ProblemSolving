from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        que = deque()
        visited = [[False for _ in range(len(A[0]))] for _ in range(len(A))]
        visited[0][0] = True
        que.append((0, 0, 0))
        maxLen = -1
        while que:
            x, y, l = que.pop()
            if x == len(A)-1 and y == len(A[0])-1:
                maxLen = max(l, maxLen)
            for posx, posy in [(1,0),(0, 1)]:
                newx = x+posx
                newy = y+posy
                if 0 <= newx < len(A) and 0 <= newy < len(A[0]):
                    if not visited[newx][newy]:
                        if A[newx][newy] > A[x][y]:
                            #print("addiing", A[newx][newy])
                            que.append((newx, newy, l+1))
        print(maxLen)
        return maxLen+1 if maxLen else -1

sol = Solution()
A = [
  [35, 1, 70, 25, 79, 59, 63, 65],
  [6, 46, 82, 28, 62, 92, 96, 43]
]
sol.solve(A)
