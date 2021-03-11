from Tree import *
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        stack = [(root, None, None)]
        for i in range(1, len(preorder)):
            val = preorder[i]
            new_node = TreeNode(val)
            node, lo, hi = stack[-1]
            if val < node.val:
                node.left = new_node
                stack.append((new_node, lo, node.val))
            else:
                while True:
                    fit = ((not lo) or lo < val) and ((not hi) or val < hi)
                    if fit: break
                    stack.pop()
                    node, lo, hi = stack[-1]
                node.right = new_node
                stack.append((new_node, node.val, hi))
        return root
                