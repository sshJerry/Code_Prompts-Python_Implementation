/*
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

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

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 */

/*
Will the array of nums ever be empty or null? No
Can we expect non integers in either nums arrays or target? No
How big is the array of nums? Not too big
Will there always be a valid answer? Yes
 */

import java.util.HashMap;
import java.util.Map;

/*
Brute force method would be use a nested for loop to check every index against t.

We can do better by using a Hash Map to check if the delta is currently in the map, if not store
the value and the index in the map and continue iterating
 */
public class LC1TwoSum1 {
    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> currentValueToIndex = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int delta = target - nums[i];
            if(currentValueToIndex.containsKey(delta)) {
                return new int[] {currentValueToIndex.get(delta), i};
            }
            currentValueToIndex.put(nums[i], i);
        }
        return new int[] {};
    }
}
// TC O(n), SC O(n)

