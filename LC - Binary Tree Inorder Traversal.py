# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Big O: If tree has n nodes, each node is visited only once. Making Big O (n)
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self._traversal(root)
        
    def _traversal(self, current):
        """
        if current:
            for node in self._traversal(current.left):
                yield node
            yield current.val
            for node in self._traversal(current.right):
                yield node
         Other Method works since Python 3 - PEP 380: Syntax for Delegating to a Subgenerator
         Link: https://docs.python.org/3/whatsnew/3.3.html#pep-380
         """
        if current:
            yield from self._traversal(current.left)
            yield current.val
            yield from self._traversal(current.right)
