# solving with DP

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        res=dp[0]
        for i in range(1,len(nums)):
            dp[i] = nums[i]
            if dp[i]<dp[i-1]+nums[i]:
                dp[i] = dp[i-1]+nums[i]
            res = max(res,dp[i])
        return res

