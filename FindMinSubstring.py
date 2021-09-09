class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        alpha_count = [0]*26
        for s in A:
            charCount = [0]*26
            for c in s:
                charCount[ord(c)-97] += 1
            for alpha, count in enumerate(charCount):
                if count:
                    if alpha_count[alpha] < count:
                        alpha_count[alpha] = count
        print("alpha_count", alpha_count)
        return sum(alpha_count)

sol = Solution()
result = sol.solve(["abcd", "cdef", "fgh", "de"])
print("minSubString", result)