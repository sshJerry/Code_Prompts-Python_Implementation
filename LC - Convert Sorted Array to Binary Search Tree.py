# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Runtime: 42 ms, faster than 97.54% of Python online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.9 MB, less than 98.26% of Python online submissions for Convert Sorted Array to Binary Search Tree.
O(n)
"""
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        l, r = 0, len(nums)-1
        return self._sort(nums,l,r)
    
    def _sort(self, arr, left, right, root = None):
        if left > right:
            return None
        middle = (left+right) //2
        root = TreeNode(arr[middle])
        root.left = self._sort(arr,left,middle-1,root)
        root.right = self._sort(arr,middle+1,right,root)
        return root
        
