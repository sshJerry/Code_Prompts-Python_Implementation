/*
Given an integer array nums, return true if any value appears
at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
 */

/*
How many elements can we expect? Not alot
How large are the numbers? Very small
Can we get negatives or zeros? You can get negatives and zero
Can we expect only integers or objects/strings? only integers
Can we get an array that's empty or null? No
 */

import java.util.HashSet;
import java.util.Set;

public class LC217ContainsDuplicate1 {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> storedNums = new HashSet<>();
        for (int num : nums){
            if (storedNums.contains(num))
                return true;
            storedNums.add(num);
        }
        return false;
    }
}
