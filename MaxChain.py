class Solution:
    def recSol(self, A, n, minval):
        print("A[n]....", A[n], "minval....", minval)
        if n < 0:
            return 0
        if n == 0:
            return 1 if A[n][1] < minval else 0
        if A[n][1] < minval:
            sol = 1 + self.recSol(A, n - 1, A[n][0])
        else:
            sol = self.recSol(A, n - 1, minval)
        return sol

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        max_ = 0
        '''
[98, 894]
[397, 942]
[70, 519]
[258, 456]
[286, 449]
[516, 626]
[370, 873]
[214, 224]
[74, 629]
[265, 886]
[708, 815]
[394, 770]
[56, 252]
        '''
        for n in range(len(A) - 1, -1, -1):
            val = self.recSol(A, n, A[n][1] + 1)
            print("for {} val is {}".format(A[n], val))
            max_ = max(max_, val)
        return max_

        mcl = [1 for i in range(len(A))]

        for i in range(1, len(A)):
            for j in range(0, i):
                if A[i][0] > A[j][1] and mcl[i] < (mcl[j] + 1):
                    mcl[i] = mcl[j] + 1
        return max(mcl)


A = [[98, 894], [397, 942], [70, 519], [258, 456], [286, 449], [516, 626],
     [370, 873], [214, 224], [74, 629], [265, 886], [708, 815], [394, 770], [56, 252]]
obj = Solution()
obj.solve(A)
