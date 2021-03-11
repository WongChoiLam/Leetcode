from Tree import *
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return None
        def sink(node : TreeNode, x : int):
            current = node
            new_node = TreeNode(x)
            while current:
                if not current.right:
                    current.right = new_node
                    break
                elif current.right.val < x:
                    new_node.left = current.right
                    current.right = new_node
                    break
                current = current.right
        root = TreeNode(nums[0])
        for i in nums[1:]:
            new_node = TreeNode(i)
            if i > root.val:
                new_node.left = root
                root = new_node
            else:
                print("sink", root.val, i)
                sink(root, i)
        return root
s = Solution()                
q = [3,2,1,6,0,5]
print(treeToList(s.constructMaximumBinaryTree(q)))
