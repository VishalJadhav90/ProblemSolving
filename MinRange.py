class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_range = 0
        max_range = sum(A)
        subsol = [[False for _ in range(max_range + 1)] for _ in range(len(A) + 1)]
        for r in range(len(A) + 1):
            subsol[r][0] = True

        for i in range(1, len(A) + 1):
            for j in range(1, max_range + 1):
                if A[i - 1] <= j:
                    subsol[i][j] = subsol[i - 1][j] or subsol[i - 1][j - A[i - 1]]
                else:
                    subsol[i][j] = subsol[i - 1][j - A[i - 1]]

        for l in subsol:
            print(l)

        min_diff = max_range
        for i in range(max_range+1):
            if subsol[len(A)][i]:
                min_diff = min(min_diff, abs(max_range - 2*i))
        return min_diff

sol = Solution()
print(sol.solve([1, 6, 11, 5]))