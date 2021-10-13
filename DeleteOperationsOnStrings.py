class Solution:
    def recSol(self, word1, word2, w1, w2):
        if w1 == len(word1) and w2 == len(word2):
            return 0
        if w1 == len(word1) and w2 < len(word2):
            return len(word2[w2:])
        if w2 == len(word2) and w1 < len(word1):
            return len(word1[w1:])
        if word1[w1] == word2[w2]:
            return self.recSol(word1, word2, w1 + 1, w2 + 1)
        else:
            return 1 + min(self.recSol(word1, word2, w1 + 1, w2), self.recSol(word1, word2, w1, w2 + 1))

    def minDistance(self, word1: str, word2: str) -> int:
        w1 = 0
        w2 = 0
        # return self.recSol(word1, word2, w1, w2)

        w1 = len(word1)
        w2 = len(word2)
        dp = [[0 for _ in range(w1 + 1)] for _ in range(w2 + 1)]
        for i in range(1, w1 + 1):
            dp[0][i] = 1 + dp[0][i - 1]
        for j in range(1, w2 + 1):
            dp[j][0] = 1 + dp[j - 1][0]  # imp
        for r in range(1, w2 + 1):
            for c in range(1, w1 + 1):
                if word2[r - 1] == word1[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1])

        return dp[w2][w1]
