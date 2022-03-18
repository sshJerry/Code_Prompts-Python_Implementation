"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        position = []
        index = 1
        for num1 in nums:
            for num2 in nums[index:]:
                if num1 + num2 == target and (nums.index(num1) != nums.index(num2, index)):
                    position = [nums.index(num1), nums.index(num2, index)]
                index = index + 1
            index = nums.index(num1)
        return position
