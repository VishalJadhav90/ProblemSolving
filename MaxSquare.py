class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        s = [[0 for c in range(cols+1)] for r in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if A[i-1][j-1] == 1:
                    s[i][j] = min(s[i][j - 1], s[i - 1][j], s[i - 1][j - 1]) + 1
                else:
                    s[i][j] = 0

        print("ssssss")
        for ss in s:
            print(ss)

        max_of_s = s[0][0]
        max_i = 0
        max_j = 0
        for i in range(rows+1):
            for j in range(cols+1):
                if max_of_s < s[i][j]:
                    max_of_s = s[i][j]
                    max_i = i
                    max_j = j
        print(max_i, max_j, max_of_s)

        count = 0
        for i in range(max_i, max_i - max_of_s, -1):
            for j in range(max_j, max_j - max_of_s, -1):
                count += 1

        print("count", count)



sol = Solution()
A = [[0, 1, 1, 0, 1],
[1, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]]

A = [
[0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
]
A = [
  [0, 0, 1],
  [1, 0, 1],
  [0, 1, 1],
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0],
  [1, 1, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 1, 0],
  [1, 1, 1],
  [1, 0, 1],
  [0, 1, 1],
  [1, 0, 1]
]
A = [
  [0],
  [0],
  [1],
  [0],
  [1],
  [1],
  [0],
  [1],
  [0],
  [0]
]
sol.solve(A)
