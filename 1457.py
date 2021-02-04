# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, node: TreeNode, path) -> int:
        if node == None : return 0
        if node.val in path:
            path.remove(node.val)
        else:
            path.append(node.val)
        if node.left == None and node.right == None and len(path) < 2: return 1
        return self.backtrack(node.left, path.copy()) + self.backtrack(node.right, path.copy())
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.backtrack(root, [])