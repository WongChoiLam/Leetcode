# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        isleaf = lambda node:node.left==None and node.right==None
        if root.left != None: root.left = self.removeLeafNodes(root.left, target)
        if root.right!= None: root.right= self.removeLeafNodes(root.right,target)
        if root.left != None and root.left.val == target and isleaf(root.left): root.left = None
        if root.right!= None and root.right.val== target and isleaf(root.right):root.right= None
        if isleaf(root):
            return None if root.val == target else root
        return root