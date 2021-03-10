from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, 1, 1)]
        while len(stack) > 0:
            node, parent_mod_2, grandparent_mod_2 = stack.pop()
            if grandparent_mod_2 == 0:
                ans += node.val
            this_mod_2 = node.val % 2
            if node.left:
                stack.append((node.left, this_mod_2, parent_mod_2))
            if node.right:
                stack.append((node.right,this_mod_2, parent_mod_2))
        return ans
            
        