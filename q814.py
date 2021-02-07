# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def prune(self, node: TreeNode) -> TreeNode:
        if(node.left != None): node.left = self.prune(node.left)
        if(node.right!= None): node.right= self.prune(node.right)
        if(node.left == None and node.right == None and node.val==0): return None
        return node
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if(root != None): root = self.prune(root)
        return root