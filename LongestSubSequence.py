class Solution:
    def recSol(self, string1, n1, string2, n2):
        if n1 == len(string1) or n2 == len(string2):
            return 0
        if string1[n1] == string2[n2]:
            return 1 + self.recSol(string1, n1+1, string2, n2+1)
        else:
            return max(self.recSol(string1, n1+1, string2, n2),
                       self.recSol(string1, n1, string2, n2+1))

    def longestSubSequence(self, string1, string2):
        n1 = len(string1)
        n2 = len(string2)
        dp = [[0 for _ in range(n1+1)] for _ in range(n2+1)]
        for r in range(1, n2+1):
            for c in range(1, n1+1):
                if string2[r-1] == string1[c-1]:
                    dp[r][c] = dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[n2][n1]

sol = Solution()
print(sol.longestSubSequence("vishal", "ihal"))