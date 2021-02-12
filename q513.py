from Tree import *

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ans = root
        current_level = 0
        
        stack = [(0,root)]
        
        while len(stack) > 0:
            level, node = stack.pop()
            if node == None: continue
            if node.left==None and node.right==None and level > current_level:
                ans = node
                current_level = level
            stack.append((level+1, node.right))
            stack.append((level+1, node.left))
        return ans.val