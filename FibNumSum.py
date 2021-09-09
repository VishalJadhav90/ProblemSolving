class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fibNum = [0, 1, 1]
        fibSet = set([0, 1])
        prev = 1
        num = 1
        while num < A:
            temp = num
            num = prev + num
            if num <= A:
                fibNum.append(num)
                fibSet.add(num)
            prev = temp

        print("fibNum", fibNum)

        if A in fibNum:
            return 1
        n = A
        count = 0
        while n > 0:
            if n in fibSet:
                n -= n
                count += 1
            else:
                pop = 0
                for ele in fibNum:
                    if ele < n:
                        pop = ele
                        continue
                    break
                count += 1
                n -= pop
        return count

sol = Solution()
print("result", sol.fibsum(64))


