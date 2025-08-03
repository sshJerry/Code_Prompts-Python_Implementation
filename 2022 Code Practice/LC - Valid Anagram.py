"""
QUESTION PROMPT:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging
 the letters of a different word or phrase, typically using all the 
original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


"""
Big O: Assuming the hashmap accessing is constant time O(1), 
       the for loop (O (n)) and the addition/subtration operations (O (1))
       The Big O is O(n).
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = 0
        if len(s) != len(t):
            return False
        for x in range(0, len(s)):
            result += hash(s[x])
            result -= hash(t[x])
        if result == 0:
            return True
        else:
            return False
  
