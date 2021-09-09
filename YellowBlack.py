class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        yellow = set()
        blue = set()
        for r1, r2 in B:
            if r1 in yellow and r2 in yellow:
                return 0
            if r2 in blue and r2 in blue:
                return 0
            if r1 in yellow:
                blue.add(r2)
            elif r1 in blue:
                yellow.add(r2)
            elif r2 in yellow:
                blue.add(r1)
            else:
                yellow.add(r1)
        return 1

sol = Solution()
A = 4
B = [[1, 4],
     [3, 1],
     [4, 3],
     [2, 1]]
ans = sol.solve(A, B)
print("ans", ans)
