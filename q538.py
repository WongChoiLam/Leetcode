from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        def post_order(acc, node : TreeNode):
            if node.right:
                acc = post_order(acc, node.right)
            acc += node.val
            node.val = acc
            if node.left:
                acc = post_order(acc, node.left)
            return acc
        post_order(0, root)
        return root