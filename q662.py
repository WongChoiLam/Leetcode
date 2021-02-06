from Tree import *
from typing import List

class Solution:
    def dfs(self, root: TreeNode):
        leftmost = {1:1}
        rightmost= {1:1}

        backtrack = [(root, 1, 1)]
        while len(backtrack) > 0:
            node, layer, index = backtrack.pop()
            if layer not in leftmost.keys(): leftmost[layer] = index
            if layer not in rightmost.keys():rightmost[layer] = index
            elif rightmost[layer] < index: rightmost[layer] = index
            if node.right!= None: backtrack.append((node.right,layer + 1, index * 2 + 1))
            if node.left != None: backtrack.append((node.left, layer + 1, index * 2))
        return leftmost, rightmost  
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None: return 0
        left, right = self.dfs(root)
        i = 1
        ans = 1
        while i in left.keys():
            width = right[i] - left[i] + 1
            if width > ans: ans = width
            i += 1
        return ans
