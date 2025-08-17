/*
Given an integer array nums, return an array answer such that answer[i]
 is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
 */
public class LC238ProductOfArrayExceptSelf {
    /*
    TC O(n^2)
    SC O(n)

    Brute force works but at scale, can suffer.
     */
    public int[] productExceptSelfBruteForce(int[] nums) {
        int[] answers = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int multipliedValue = 1;
            for (int j = 0; j < nums.length; j++) {
                if (i == j)
                    continue;
                multipliedValue = multipliedValue * nums[j];
            }
            answers[i] = multipliedValue;
        }
        return answers;
    }

    /*
    TC O(n+n+n) = O(n)
    SC O(n+n+n) = O(n)

    More efficient. By taking linear time complexity, we speed up runtime of operation and while at worst,
    on average, consuming the same amount of space. This can be improved by calculating answers on the fly
    while respecting the prompts request of not using division.

    Next time working on this problem, prioritize calculation on the fly.
     */
    public int[] productExceptSelf(int[] nums) {
        int[] answers = new int[nums.length];
        int productLeftOfIndex = 1;
        int productRightOfIndex = 1;
        int[] productRightOfIndexArray = new int[nums.length];
        int[] propuctLeftOfIndexArray = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                propuctLeftOfIndexArray[i] = productLeftOfIndex;
                continue;
            }
            productLeftOfIndex = productLeftOfIndex * nums[i - 1];
            propuctLeftOfIndexArray[i] = productLeftOfIndex;

        }
        for (int j = nums.length - 1; j >= 0; j--) {
            if (j == nums.length - 1) {
                productRightOfIndexArray[j] = productRightOfIndex;
                continue;
            }
            productRightOfIndex = productRightOfIndex * nums[j + 1];
            productRightOfIndexArray[j] = productRightOfIndex;
        }
        for (int x = 0; x < nums.length; x++) {
            answers[x] = propuctLeftOfIndexArray[x] * productRightOfIndexArray[x];
        }
        return answers;
    }
}
