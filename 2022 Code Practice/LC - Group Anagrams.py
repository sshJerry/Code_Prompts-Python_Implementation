"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging
 the letters of a different word or phrase, typically using all the 
original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


"""
Big O: Hide your eyes. It works but it O(n Log n) time. 
Had to find a roundabout solution for the following test cases ["",""] and ["a","a"]
"""

def isAnagram(s, t):
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


class Solution(object):
    def groupAnagrams(self, strs):
        listSet = set()
        newList, tempList = [], []
        if len(strs) == 1:
            return [strs]
        for x in range(0, len(strs)):
            if strs[x] in listSet:
                continue
            else:
                listSet.add(strs[x])
                tempList = [strs[x]]
            for y in range(strs.index(strs[x]), len(strs)):
                if strs[y] in listSet:
                    if y == x:
                        continue
                    if isAnagram(strs[x], strs[y]):
                        tempList.append(strs[y])
                        continue
                if isAnagram(strs[x], strs[y]):
                    tempList.append(strs[y])
                    listSet.add(strs[y])
            newList.append(tempList)
        return newList

e = Solution()
#Test Case 1
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(e.groupAnagrams(strings))
#Test Case 2
strings = ["",""]
print(e.groupAnagrams(strings))
#Test Case 3
strings = ["","b"]
print(e.groupAnagrams(strings))
#Test Case 4
strings = ["c","c"]
print(e.groupAnagrams(strings))
