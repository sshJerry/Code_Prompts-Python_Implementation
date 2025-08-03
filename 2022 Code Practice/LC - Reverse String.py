"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution(object):
    def reverseString(self, s):
        posa, posb = 0, len(s) - 1
        while not posa > posb:
            s[posa], s[posb] = s[posb], s[posa]
            posb -= 1
            posa += 1
