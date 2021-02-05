# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, node: TreeNode, parent, left) -> bool:
        xor = lambda x,y : not ((x and y) or (not (x or y)))
        if node == None: return True
        for i,p in enumerate(parent):
            if xor(node.val<p, left[i]) or node.val==p:return False
        return self.validate(node.left, parent+[node.val], left + [True]) and self.validate(node.right, parent+[node.val],left + [False])
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, [], [])