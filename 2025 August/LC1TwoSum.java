import java.util.HashMap;
import java.util.Map;

/*
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 *
 * Example 1:
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 *
 * Example 2:
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 *
 * Example 3:
 * Input: nums = [3,3], target = 6
 * Output: [0,1]

 * Constraints:
 * 2 <= nums.length <= 104
 * -109 <= nums[i] <= 109
 * -109 <= target <= 109
 * Only one valid answer exists.
 * Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 */
public class LC1TwoSum {
    public int[] twoSum(int[] nums, int target) {
        /*
         * Questioning
         * Can nums or target be null or empty? No
         * Will we always have at least two integers in the nums array? Yes
         * Will I always find an answer? Yes
         * How large can the array of ints be? Very Large
         * How big are numbers within nums and target? Very Large
         * Can they be negative? Yes
         *
         * Test Cases
         * nums = [-15,7,11,15], target = -8
         * Output: [0, 1]
         *
         * nums = [-1000, 1000], target = 0
         * Output: [0, 1]
         *
         * nums = [0, 1, 2, 3, 4, 5, 6, 7], target = 13
         * Output: [6, 7]
         */

        /*
         * There's the obvious brute force approach where we have a nested loop that iterates through the array
         * and doing arithmetic at every step to get if the two indexes equal the target.
         *
         * At worst this is
         * TC O(n^2)
         * SC O(n)
         *
         * Goal is to get TC O(n) time.
         *
         * The thing is, given I'm currently at a number, what does the second number have to be to equal my target.
         * I'm thinking a hashmap where the key is the current value and the value is the index. After an iteration
         * check if the delta is in the map
         *
         * TC O(n)
         * SC O(n)
         *
         */

        Map<Integer, Integer> valueToIndexMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int delta = target - nums[i];
            if (valueToIndexMap.containsKey(delta))
                return new int[]{valueToIndexMap.get(delta), i};
            valueToIndexMap.put(nums[i], i);
        }
        return new int[0];

    }
}
