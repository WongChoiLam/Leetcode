# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sub_min(node:TreeNode) -> int:
        while node.left != None:
            node = node.left
        return node.val
    def sub_max(node:TreeNode) -> int:
        while node.right != None:
            node = node.right
        return node.val
    def getMinimumDifference(self, root: TreeNode) -> int:
        minimum = None
        if root.left != None:
            minimum = root.val - Solution.sub_max(root.left)
            if root.right != None:
                minimum = min(minimum, Solution.sub_min(root.right) - root.val)
        else:
            minimum = Solution.sub_min(root.right) - root.val
        if root.left != None and not (root.left.left == None and root.left.right == None):
            minimum = min(minimum, self.getMinimumDifference(root.left))
        if root.right != None and not (root.right.left == None and root.right.right == None):
            minimum = min(minimum, self.getMinimumDifference(root.right))
        return minimum