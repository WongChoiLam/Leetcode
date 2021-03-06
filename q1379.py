from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while len(stack) > 0:
            oNode, cNode = stack.pop()
            if oNode == None: continue
            if oNode is target:
                return cNode
            stack.append((oNode.left, cNode.left))
            stack.append((oNode.right,cNode.right))
        return None