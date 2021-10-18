class Solution:
    def integerBreak(self, n):
        dp = [None]
        for i in range(1, n+1):
            dp.append(i)
        print("dp", dp)
        for k in range(2, n+1):
            i = 1
            j = k-1
            maxpro = 0
            while i <= j:
                maxpro = max(maxpro, max(i, dp[i]) * max(j, dp[j]))
                i += 1
                j -= 1
            dp[k] = maxpro
        print("dp", dp)
        return dp[n]

sol = Solution()
print("result", sol.integerBreak(8))
