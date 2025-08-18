/*
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

 */

/*
Can this array be null or empty? Yes
Can we expect a non integer element? Do not expect non integer elements
    If so, can we expect whitespace? N/A
How big is this array? Not that big
If we expect only integer elements, can we expect negatives? Yes
Can we expect duplicates? Yes
 */

import java.util.HashSet;
import java.util.Set;

public class LC128LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        int longestSequence = 1;
        if (nums.length <= 1)
            return nums.length;
        for (int num : nums){
            numsSet.add(num);
        }
        for (int num : numsSet) {
            if (!numsSet.contains(num - 1)){
                int currentLongest = 1;
                int currentNumber = num;
                while (numsSet.contains(currentNumber + 1)){
                    currentLongest++;
                    currentNumber++;
                }
                longestSequence = Integer.max(longestSequence, currentLongest);
            }
        }
        return longestSequence;
    }
}
