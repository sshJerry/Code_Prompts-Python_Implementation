# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        self.invert(root)
        return root
    
    def invert (self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert (node.right)
        
