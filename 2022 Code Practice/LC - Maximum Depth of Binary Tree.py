"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

<THERE IS A PICTURE HERE>

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        currentHeight = 0
        if root!=None:
            return self._highestLevel(root, currentHeight)
        else:
            return currentHeight
        
    def _highestLevel(self, currentVal, height):
        if currentVal==None: return height
        leftside = self._highestLevel(currentVal.left, height+1)
        rightside = self._highestLevel(currentVal.right, height+1)
        return max (leftside, rightside)
