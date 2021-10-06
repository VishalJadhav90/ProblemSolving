class Solution:
    def recSol(self, nums, sol):
        if len(sol) == len(nums):
            perm = [nums[i] for i in sol]
            self.solution.add(tuple(perm))
            return
        for i in range(len(nums)):
            if i not in sol:
                self.recSol(nums, sol + [i])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.solution = set()
        for i in range(len(nums)):
            self.recSol(nums, [i])
        # print("self.solution...", self.solution)
        return self.solution

sol = Solution()

assert sol.permuteUnique([1,1,2]), [[1,2,1],[2,1,1],[1,1,2]]

