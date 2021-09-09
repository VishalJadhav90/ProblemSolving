class Solution:
    def giveMeNumsInSqr(self, A, r, c):
        sq_low_r = (r // 3) * 3
        sq_hig_r = sq_low_r + 3
        sq_low_c = (c // 3) * 3
        sq_hig_c = sq_low_c + 3
        elements = set()
        for rr in range(sq_low_r, sq_hig_r):
            for cc in range(sq_low_c, sq_hig_c):
                if A[rr][cc] != '.':
                    elements.add(A[rr][cc])
        return elements

    def giveMeNumsInRow(self, A, r):
        elements = set()
        for i in range(len(A[0])):
            elements.add(A[r][i])
        return elements

    def giveMeNumsInCol(self, A, c):
        elements = set()
        for i in range(len(A)):
            elements.add(A[i][c])
        return elements

    def givePossiblePositions(self, A, r, c):
        elements1 = self.giveMeNumsInSqr(A, r, c)
        elements2 = self.giveMeNumsInRow(A, r)
        elements3 = self.giveMeNumsInCol(A, c)
        elements = set()
        elements.update(elements1)
        elements.update(elements2)
        elements.update(elements3)
        return set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) - elements

    def giveMeNextRowCol(self, A, r, c):
        nc = c + 1
        nr = r
        if nc >= len(A):
            nr += 1
            nc = 0
        # print("for r: {} c: {} --> nr: {} nc: {}".format(r,c,nr,nc))
        return nr, nc

    def recursiveSol(self, A, r, c):
        if r >= (len(A)) and c == 0:
            print("reached here")
            for r in A:
                print(r)
            return True
        if A[r][c] != '.':
            nr, nc = self.giveMeNextRowCol(A, r, c)
            #print("r1..", r, "c..", c, "nr..", nr, "nc..", nc)
            sol = self.recursiveSol(A, nr, nc)
            if sol == True:
                return True
            return False
        for pos in self.givePossiblePositions(A, r, c):
            #print("for r {} c {} pos {}".format(r, c, pos))
            A[r][c] = pos
            nr, nc = self.giveMeNextRowCol(A, r, c)
            #print("r2..", r, "c..", c, "nr..", nr, "nc..", nc)
            sol = self.recursiveSol(A, nr, nc)
            if sol == True:
                return True
            A[r][c] = '.'
        else:
            #print("no possible sol for r.. {} and c.. {}".format(r, c))
            pass
        return False

    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        # print("---------------")
        # for l in A:
        #     print(l)
        # print("---------------")
        # print(self.giveMeNumsInSqr(A, 7, 7))
        self.recursiveSol(A, 0, 0)
        # r, c = self.giveMeNextRowCol(A, 0, 8)
        # print("r", r, "c", c)


sol = Solution()
sol.solveSudoku([
['5', '3', '.', '.', '7', '.', '.', '.', '.'],
['6', '.', '.', '1', '9', '5', '.', '.', '.'],
['.', '9', '8', '.', '.', '.', '.', '6', '.'],
['8', '.', '.', '.', '6', '.', '.', '.', '3'],
['4', '.', '.', '8', '.', '3', '.', '.', '1'],
['7', '.', '.', '.', '2', '.', '.', '.', '6'],
['.', '6', '.', '.', '.', '.', '2', '8', '.'],
['.', '.', '.', '4', '1', '9', '.', '.', '5'],
['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]
)