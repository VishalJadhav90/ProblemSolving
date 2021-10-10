class Solution:
    def clearSol(self, nums):
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            ans += dp[i]
        return ans

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return self.clearSol(nums)

        if len(nums) <= 1:
            return 0
        total = 0
        seqstart = 0
        subarrays = 0
        diff = nums[1] - nums[0]
        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) == diff:
                window = (i - seqstart) + 1
                if window == 3:
                    subarrays = 1
                else:
                    subarrays = subarrays + window - 2
            else:
                total += subarrays
                subarrays = 0
                seqstart = i - 1
                diff = nums[i] - nums[i - 1]
        total += subarrays
        return total
