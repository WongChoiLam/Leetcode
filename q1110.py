from Tree import *
from typing import List

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        parent = TreeNode()
        stack = [root]
        delete_set = set(to_delete)
        if root!=None and (not root.val in delete_set): ans.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node == None: continue
            stack.append(node.left)
            stack.append(node.right)
            if node.val in delete_set:
                if node.left != None and (not node.left.val in delete_set):
                    ans.append(node.left)
                if node.right!= None and (not node.right.val in delete_set):
                    ans.append(node.right)
            else:
                if node.left != None and (node.left.val in delete_set): node.left = None
                if node.right!= None and (node.right.val in delete_set): node.right = None
        return ans

s = Solution()
to_delete = [3,5]
root = listToTree([1,2,3,4,5,6,7])
forest = s.delNodes(root, to_delete)
for t in forest:
    print(treeToList(t))