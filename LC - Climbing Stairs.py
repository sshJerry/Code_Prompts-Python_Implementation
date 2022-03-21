"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


# Iterative Method | Runtime: 22ms    | Memory Usage: 13.4MB
class Solution(object):
    def climbStairs(self, n):
        amount = [0,1,2]
        for x in range(3,n+1):
            amount.append(amount[x-1] + amount[x-2])
        return amount[n]

s = Solution()
#Test Case 1
print(s.climbStairs(5))
#Test Case 2
print(s.climbStairs(38))

#Recursive Method, although it takes too long. Inefficent for this problem
def climbStairs(self, n):
    if n <= 1:
        return 1
    else:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
