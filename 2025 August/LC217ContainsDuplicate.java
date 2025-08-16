import java.util.HashMap;
import java.util.Map;

/*
 * Given an integer array nums, return true if any value appears at least twice in the array,
 * and return false if every element is distinct.

 * Example 1:
 * Input: nums = [1,2,3,1]
 * Output: true
 *
 * Explanation:
 * The element 1 occurs at the indices 0 and 3.
 * Example 2:
 * Input: nums = [1,2,3,4]
 * Output: false
 *
 * Explanation:
 * All elements are distinct.
 * Example 3:
 * Input: nums = [1,1,1,3,3,4,3,2,4,2]
 * Output: true

 * Constraints:
 * 1 <= nums.length <= 105
 * -109 <= nums[i] <= 109
 */
public class LC217ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        // INPUT
        // Always at least one num in int array
        // Either large negative or positive
        // OUTPUT
        // TRUE OR FALSE

        // TEST CASES
        // [1, 2, 3, 4] => False
        // [1, 2, 3, 1] => True
        // [1, 1, 1, 1] => True

        // Goal
        // O(n) or O(n log n) Time

        // if nums NULL or Empty Return False
        // This isn't necessary but good general practice
        // Map<Integer, Integer>
        if (nums == null || nums.length == 0)
            return false;
        Map<Integer, Integer> numberCount = new HashMap<>();
        for (int number : nums) {
            // Check if number exists in map
            // return true
            // Add number to map
            if (numberCount.get(number) != null)
                return true;
            numberCount.put(number, 1);
        }
        return false;
    }
}

/*
 * Notes: O(n) for Time and Space, in the worse case. Frequency Counting works, just use HashSet
 * instead of Hashmap
 */
