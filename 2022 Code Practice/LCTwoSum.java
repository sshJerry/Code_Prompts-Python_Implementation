/*
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

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
*/


import java.util.Arrays;

public class LCTwoSum {
    public static int[] twoSum(int[] nums, int target) {
        int arrayLength = nums.length;
        for (int currentIndex = 0; currentIndex < arrayLength - 1; currentIndex++) {
            for (int currentSubIndex = currentIndex + 1; currentSubIndex < arrayLength; currentSubIndex++) {
                if (target == nums[currentIndex] + nums[currentSubIndex]) {
                    return new int[]{currentIndex, currentSubIndex};
                }
            }
        }
        return new int[]{-1, -1};
    }

    public static void assertTwoSum() throws RuntimeException {
        assert Arrays.equals(twoSum(new int[]{2, 7, 11, 15}, 9), new int[]{0, 1});
        assert Arrays.equals(twoSum(new int[]{3, 2, 4}, 6), new int[]{1, 2});
        assert Arrays.equals(twoSum(new int[]{3, 3}, 6), new int[]{0, 1});
        assert !Arrays.equals(twoSum(new int[]{3, 4}, 6), new int[]{0, 1});
    }
}
