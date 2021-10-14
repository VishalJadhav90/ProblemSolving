class Solution:
    def recSol(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1 and word2:
            return len(word2)
        if not word2 and word1:
            return len(word1)
        if word1[0] == word2[0]:
            return self.recSol(word1[1:], word2[1:])
        insert = 1 + self.recSol(word1, word2[1:])
        delete = 1 + self.recSol(word1[1:], word2)
        replace = 1 + self.recSol(word1[1:], word2[1:])
        return 1 + min(insert, delete, replace)

    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        dp = [[0 for _ in range(w1 + 1)] for _ in range(w2 + 1)]
        for i in range(w1 + 1):
            dp[0][i] = i
        for i in range(w2 + 1):
            dp[i][0] = i
        for r in range(1, w2 + 1):
            for c in range(1, w1 + 1):
                if word2[r - 1] == word1[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
        return dp[w2][w1]
