from Tree import *

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def recursion(node: TreeNode) -> int:
            if node == None: return 0,0
            left_remain, left_step = recursion(node.left)
            right_remain,right_step= recursion(node.right)
            step = left_step + right_step
            remain = node.val + left_remain + right_remain - 1
            step += abs(left_remain)
            step += abs(right_remain)
            return remain,step
        return recursion(root)[1]

root = listToTree([0,3,0])
print(Solution().distributeCoins(root))