from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST_1(self, root: TreeNode) -> TreeNode:
        # recursion approach
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
    def convertBST_2(self, root: TreeNode) -> TreeNode:
        # w/o recursion
        if not root: return root
        greater_sum = 0
        stack = [(root, False)]
        while len(stack) > 0:
            node, visited = stack.pop()
            if visited:
                greater_sum += node.val
                node.val = greater_sum
                if node.left:
                    stack.append((node.left, False))
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
        return root