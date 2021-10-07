import string
class Solution:
    def workComb(self, allowedLetters, s, width, comb):
        if s == width:
            if "".join(comb):
                self.solution.append("".join(comb))
            return
        for char in allowedLetters[s]:
            self.workComb(allowedLetters, s+1, width, comb+[char])

    def letterCombinations(self, digits: str) -> List[str]:
        numAlphaDict = {2: 'abc',
                       3: 'def',
                       4: 'ghi',
                       5: 'jkl',
                       6: 'mno',
                       7: 'pqrs',
                       8: 'tuv',
                       9: 'wxyz'}
        width = len(digits)
        allowedLetters = [numAlphaDict[int(num)] for num in digits]
        #print("allowedLetters", allowedLetters)
        self.solution = []
        self.workComb(allowedLetters, 0, width, [])
        #print("self.solution", self.solution)
        return self.solution

sol = Solution()
assert sol.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"]
