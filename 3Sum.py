class Solution:
    def threeSumPairs(self, nums):
        sol = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    sol.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return sol

solution = Solution()
print(solution.threeSumPairs([-4, -2, -1, 0, 1, 2]))
