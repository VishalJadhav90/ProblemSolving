class Solution:
    def findMinJumps(self, nums, pos, jumps):
        if pos >= len(nums)-1:
            print("jumps", jumps)
            self.minjumps = min(self.minjumps, jumps)
            return
        if nums[pos] == 0:
            return
        for moves in range(1, nums[pos]+1):
            self.findMinJumps(nums, pos+moves, jumps+1)

    def jump(self, nums):
        self.minjumps = float('inf')
        #self.findMinJumps(nums, 0, 0)

        left, right = 0, nums[0]
        self.minjumps = 1
        while right < len(nums)-1:
            self.minjumps += 1
            nxt = max(i+nums[i] for i in range(left, right+1))
            left, right = right, nxt
        return self.minjumps

sol = Solution()
print("ans", sol.jump([2,3,0,1,4]))

