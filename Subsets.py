class Solution:
    def recSol(self, nums, pos, sol):
        self.solution.append(sol)
        for adj in range(pos+1,len(nums)):
            self.recSol(nums, adj, sol+[nums[adj]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.solution = [[]]
        for i in range(len(nums)):
            self.recSol(nums, i, [nums[i]])
        #print("self.solution", self.solution)
        return self.solution
