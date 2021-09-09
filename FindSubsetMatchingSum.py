class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        subsol = [[False for _ in range(B+1)] for _ in range(len(A)+1)]
        for i in range(len(A)+1):
            subsol[i][0] = True
        for j in range(B+1):
            subsol[0][j] = False

        for i in range(1, len(A)+1):
            for j in range(1, B+1):
                if A[i-1] <= j:
                    subsol[i][j] = subsol[i-1][j] or subsol[i-1][j-A[i-1]]
                else:
                    subsol[i][j] = subsol[i-1][j]
        return subsol[len(A)][B]


sol = Solution()
