from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ret = 0
        max_layer = 0
        stack = [(root,0)]
        while len(stack) > 0:
            node, layer = stack.pop()
            if node.left == None and node.right == None:
                if layer == max_layer:
                    ret += node.val
                elif layer > max_layer:
                    ret = node.val
                    max_layer = layer
                continue
            if node.left:
                stack.append((node.left, layer + 1))
            if node.right:
                stack.append((node.right,layer + 1))
        return ret
                