"""
Runtime: 798 ms, faster than 77.38% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28 MB, less than 41.04% of Python3 online submissions for Maximum Subarray.
O(n)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)
