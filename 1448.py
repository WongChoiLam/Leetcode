# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes_aux(self, node:TreeNode, path_max:int) -> int:
        if node == None: return 0
        if node.val >= path_max:
            return 1 + self.goodNodes_aux(node.left, node.val) + self.goodNodes_aux(node.right, node.val)
        return self.goodNodes_aux(node.left, path_max) + self.goodNodes_aux(node.right, path_max)
    def goodNodes(self, root: TreeNode) -> int:
        if root == None: return 0
        return 1 + self.goodNodes_aux(root.left, root.val) + self.goodNodes_aux(root.right, root.val)